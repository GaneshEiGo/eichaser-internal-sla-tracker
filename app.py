"""
========================================================================================================================
  ███████╗██╗   ██╗██████╗ ██████╗ ██╗███████╗██╗███████╗
  ██╔════╝██║   ██║██╔══██╗██╔══██╗██║██╔════╝██║██╔════╝
  █████╗  ██║   ██║██████╔╝██████╔╝██║█████╗  ██║█████╗
  ██╔══╝  ██║   ██║██╔══██╗██╔══██╗██║██╔══╝  ██║██╔══╝
  ███████╗╚██████╔╝██████╔╝██║  ██║██║██║     ██║███████╗
  ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝

  EiChaser Universal :: The Universal Commitment OS
  Version : 3.0.0 "Glass Intelligence"
  Author  : Kaduri Ganesh
================================================================================
  "Every commitment is a promise. Every promise has a clock."
================================================================================
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import time
import uuid
import random
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

import streamlit as st
import streamlit.components.v1 as components

from dotenv import load_dotenv

try:
    import google.generativeai as genai
    _HAS_GENAI = True
except ImportError:
    _HAS_GENAI = False

# ----------------------------------------------------------------------------
# GEMINI CONFIGURATION
# ----------------------------------------------------------------------------

load_dotenv()

_GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
_GEMINI_MODEL = "gemini-1.5-pro"

APP_NAME = "EiChaser Universal"
APP_TAGLINE = "The Universal Commitment OS"
APP_VERSION = "2.0.0 Glass Intelligence"
DB_FILE = "eichaser_universal.db"

# ============================================================================
# DATA MODELS & STALL ENGINE
# ============================================================================

SEVERITY_WEIGHTS = {
    "critical": 1.50,
    "high":     1.20,
    "medium":   1.00,
    "low":      0.75
}

def get_reliability_modifier(score: float) -> float:
    if score >= 0.90: return 0.85
    if score >= 0.75: return 1.00
    if score >= 0.50: return 1.15
    return 1.30

BLAST_RADIUS_FACTORS = {
    "Isolated": 1.00,
    "Multi-Team": 1.25,
    "Critical Path": 1.50
}

@dataclass
class Commitment:
    id: str
    industry: str
    text: str
    owner: str
    promised_time: str
    expected_minutes: int
    severity: str
    reliability: float
    blast_radius: str
    artifact: str
    dependency: str
    status: str = "Open"
    
    @property
    def time_elapsed_minutes(self) -> float:
        try:
            pt = datetime.fromisoformat(self.promised_time)
            return max(0, (datetime.now() - pt).total_seconds() / 60)
        except:
            return 0

    @property
    def stall_score(self) -> float:
        if self.status == "Resolved": return 0
        time_ratio = self.time_elapsed_minutes / self.expected_minutes if self.expected_minutes > 0 else 1
        sev = SEVERITY_WEIGHTS.get(self.severity.lower(), 1.0)
        rel = get_reliability_modifier(self.reliability)
        blast = BLAST_RADIUS_FACTORS.get(self.blast_radius, 1.0)
        score = min(100.0, time_ratio * 100 * sev * rel * blast)
        return round(score, 1)

    @property
    def risk_tier(self) -> str:
        s = self.stall_score
        if s >= 85: return "Critical"
        if s >= 65: return "Stalled"
        if s >= 40: return "At Risk"
        return "On Track"

    @property
    def diagnosis(self) -> str:
        """Deterministic 'Why is it stuck?' logic"""
        if self.status == "Resolved": return "Completed"
        if self.dependency != "None" and self.dependency and self.stall_score > 60:
            return "Dependency Delay"
        if self.reliability < 0.70 and self.stall_score > 50:
            return "Capacity Conflict"
        if self.stall_score > 40:
            return "Silence Duration"
        return "Normal Cadence"

    def to_html_row(self) -> str:
        tier = self.risk_tier
        tier_color = "var(--rose)" if tier == "Critical" else "var(--amber)" if tier == "Stalled" else "var(--sky)" if tier == "At Risk" else "var(--emerald)"
        bg_color = "var(--rose-softer)" if tier == "Critical" else "var(--amber-softer)" if tier == "Stalled" else "var(--sky-softer)" if tier == "At Risk" else "var(--bg-elevated)"
        diag_badge = "var(--graphite-500)" if self.diagnosis == "Normal Cadence" else tier_color
        
        return f"""
        <div class="commitment-row" style="background: {bg_color}; border-left: 3px solid {tier_color};">
            <div class="row-top">
                <div class="row-left">
                    <span class="pixel-badge" style="background: {tier_color}; color: white; border: none;">{tier}</span>
                    <strong class="commitment-text">{self.text}</strong>
                </div>
                <span class="stall-score" style="color: {tier_color};">{self.stall_score}</span>
            </div>
            <div class="row-bottom">
                <span><strong>Owner:</strong> {self.owner}</span>
                <span><strong>Industry:</strong> {self.industry}</span>
                <span><strong>Impact:</strong> {self.blast_radius}</span>
                <span style="color: {diag_badge};"><strong>Diagnosis:</strong> {self.diagnosis}</span>
            </div>
        </div>
        """

# ============================================================================
# INDUSTRY ARCHETYPES & SEED DATA
# ============================================================================
INDUSTRIES = [
    "Software & SRE", "Civil & Construction", "Electrical & Utilities", "Healthcare & Clinical",
    "Industrial & Manufacturing", "Legal & Commercial", "Finance & Banking", "Supply Chain",
    "Cybersecurity", "Aerospace & Defense"
]

SEED_COMMITMENTS = [
    ("Software & SRE", "Raise Redis connection pool limit for checkout service", "Alex (Platform Eng)", 120, "high", 0.95, "Multi-Team", "Config File", "None"),
    ("Civil & Construction", "Submit 28-day concrete compression lab certificate for Pier Cap 4", "Rajesh (Geotech)", 2880, "critical", 0.60, "Critical Path", "Lab Certificate", "Concrete Testing Lab"),
    ("Electrical & Utilities", "Grant Line Clear (LC) approval for Feeder 3 transformer energization", "Vikram (Discom)", 480, "critical", 0.85, "Critical Path", "LC Permit", "State Transmission Utility"),
    ("Healthcare & Clinical", "Post blood culture sensitivity report for ICU Bed 8", "Dr. Chen (Microbiology)", 720, "high", 0.88, "Isolated", "Lab Results", "LIMS System"),
    ("Industrial & Manufacturing", "Sign off on First Article Inspection (FAI) for CNC Batch 47", "Sarah (QA)", 240, "medium", 0.92, "Multi-Team", "FAI Report", "Metrology Lab"),
    ("Legal & Commercial", "Return indemnification clause redlines for Enterprise Contract", "David (Outside Counsel)", 600, "high", 0.70, "Isolated", "Redlined PDF", "Partner Review"),
    ("Finance & Banking", "File Suspicious Activity Report (SAR) for Alert FRD-84729", "Maria (Compliance)", 14400, "high", 0.99, "Critical Path", "SAR Filing", "FinCEN Portal"),
    ("Cybersecurity", "Patch CVE-2024-8472 on production firewall cluster", "James (SecOps)", 360, "critical", 0.95, "Multi-Team", "Deployment Ticket", "Change Advisory Board"),
    ("Supply Chain", "Confirm container ETA for Port of Long Beach", "Lee (Logistics)", 180, "medium", 0.80, "Isolated", "Shipping Manifest", "Port Authority"),
    ("Aerospace & Defense", "Review DO-178C MC/DC coverage gaps for flight-control software", "Robert (Software)", 2880, "high", 0.65, "Critical Path", "Coverage Report", "QA Verification")
]

def _h(html: str) -> str:
    """Strip indentation and blank lines so Streamlit renders HTML, not code."""
    lines = [ln.strip() for ln in html.splitlines()]
    return "\n".join(ln for ln in lines if ln)

# ============================================================================
# DATABASE LAYER (Robust Auto-Migration)
# ============================================================================
def _db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    
    # Check existing schema
    table_info = conn.execute("PRAGMA table_info(commitments)").fetchall()
    if table_info:
        cols = [row[1] for row in table_info]
        required_cols = ["id", "industry", "text", "owner", "promised_time", "expected_minutes", "severity", "reliability", "blast_radius", "artifact", "dependency", "status"]
        if not all(rc in cols for rc in required_cols):
            conn.execute("DROP TABLE IF EXISTS commitments")
            table_info = [] # Reset to trigger creation
            
    if not table_info:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS commitments (
                id TEXT PRIMARY KEY,
                industry TEXT,
                text TEXT,
                owner TEXT,
                promised_time TEXT,
                expected_minutes INTEGER,
                severity TEXT,
                reliability REAL,
                blast_radius TEXT,
                artifact TEXT,
                dependency TEXT,
                status TEXT DEFAULT 'Open'
            )
        """)
        conn.commit()
    
    # Seed if empty
    count = conn.execute("SELECT COUNT(*) FROM commitments").fetchone()[0]
    if count == 0:
        for ind, txt, own, exp, sev, rel, blast, art, dep in SEED_COMMITMENTS:
            promised = (datetime.now() - timedelta(minutes=random.randint(10, 3000))).isoformat()
            cid = hashlib.md5(f"{ind}:{txt}:{uuid.uuid4()}".encode()).hexdigest()[:12]
            conn.execute("INSERT INTO commitments VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", 
                         (cid, ind, txt, own, promised, exp, sev, rel, blast, art, dep, "Open"))
        conn.commit()
    return conn

def load_commitments(industry_filter: str = "All") -> List[Commitment]:
    with _db() as conn:
        if industry_filter == "All":
            rows = conn.execute("SELECT * FROM commitments ORDER BY promised_time ASC").fetchall()
        else:
            rows = conn.execute("SELECT * FROM commitments WHERE industry=? ORDER BY promised_time ASC", (industry_filter,)).fetchall()
        
        return [Commitment(
            id=r[0], industry=r[1], text=r[2], owner=r[3], promised_time=r[4],
            expected_minutes=r[5], severity=r[6], reliability=r[7], blast_radius=r[8], 
            artifact=r[9], dependency=r[10], status=r[11]
        ) for r in rows]

def update_commitment_status(cid: str, status: str):
    with _db() as conn:
        conn.execute("UPDATE commitments SET status=? WHERE id=?", (status, cid))
        conn.commit()

# ============================================================================
# LLM SYNTHESIS ENGINE (Hyper-Human Tone)
# ============================================================================
def _configure_gemini() -> bool:
    if not _HAS_GENAI: return False
    try:
        genai.configure(api_key=_GEMINI_API_KEY)
        return True
    except Exception:
        return False

def generate_pod_action_brief(commitments: List[Commitment]) -> str:
    if not _configure_gemini(): return _fallback_brief(commitments)
    
    stalled = [c for c in commitments if c.status == "Open" and c.stall_score >= 40]
    stalled.sort(key=lambda x: x.stall_score, reverse=True)
    top_items = stalled[:5]
    
    if not top_items: return "All systems are nominal. No stalled commitments detected."
    
    data_str = "\n".join([f"- Industry: {c.industry} | Commitment: {c.text} | Owner: {c.owner} | Score: {c.stall_score} | Impact: {c.blast_radius} | Diagnosis: {c.diagnosis}" for c in top_items])
    
    prompt = f"""You are the Chief of Staff for a global operations team. Write a 'Pod Action Brief' in plain, accessible, human-friendly English. 
    Do not use emojis. Do not use technical jargon. Explain things so a non-technical executive can understand the real-world impact instantly.
    
    Format EXACTLY as follows:
    ### Story of the Day
    (1-2 sentences summarizing the biggest operational risk right now in plain English).
    
    ### Critical Action Required
    (3 bullet points of the most severe stalls, explaining *why* it matters to the business).
    
    ### System Health
    (1 sentence on overall team reliability).
    
    Commitments Data:
    {data_str}"""
    
    try:
        model = genai.GenerativeModel(_GEMINI_MODEL)
        resp = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=0.4, max_output_tokens=800))
        return resp.text
    except Exception:
        return _fallback_brief(commitments)

def _fallback_brief(commitments: List[Commitment]) -> str:
    stalled = [c for c in commitments if c.status == "Open" and c.stall_score >= 65]
    if not stalled: return "All systems are nominal. No critical stalls detected."
    lines = ["### Story of the Day", f"We have {len(stalled)} critical commitments that are currently stalled and blocking progress.", "", "### Critical Action Required"]
    for c in stalled[:3]:
        lines.append(f"- {c.text} (Owner: {c.owner}) is at a stall score of {c.stall_score}. This is impacting {c.blast_radius}.")
    lines.append("\n### System Health\nReliability is currently mixed. Immediate intervention required on top items.")
    return "\n".join(lines)

def generate_nudge(commitment: Commitment) -> str:
    if not _configure_gemini(): return _fallback_nudge(commitment)
    
    tier = commitment.risk_tier
    tone = "Gentle and collaborative" if tier == "At Risk" else "Direct and firm" if tier == "Stalled" else "Urgent and high-visibility"
    
    prompt = f"""You are EiTone, an empathetic AI assistant writing a nudge message for a stalled commitment. 
    Do not use emojis. Write in plain, accessible English. Assume positive intent. Never sound punitive. Sound like a helpful colleague.
    
    Context:
    - Commitment: {commitment.text}
    - Owner: {commitment.owner}
    - Industry: {commitment.industry}
    - Impact: {commitment.blast_radius}
    - Expected Artifact: {commitment.artifact}
    - Dependency (if any): {commitment.dependency}
    - Stall Score: {commitment.stall_score} (Tier: {tier})
    - Diagnosis: {commitment.diagnosis}
    - Tone: {tone}
    
    Write a 2-3 sentence message that includes:
    1. A friendly greeting using the owner's first name.
    2. Direct Context Bridge (reference the specific commitment and artifact).
    3. The Operational Impact (why it matters now).
    4. Frictionless Resolution (ask for a quick status update or if they are blocked).
    """
    
    try:
        model = genai.GenerativeModel(_GEMINI_MODEL)
        resp = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=0.5, max_output_tokens=300))
        return resp.text
    except Exception:
        return _fallback_nudge(commitment)

def _fallback_nudge(c: Commitment) -> str:
    return f"Hi {c.owner.split(' ')[0]}, just checking in on {c.text}. We're at a stall score of {c.stall_score} and it's impacting {c.blast_radius}. Let us know if you're blocked or need support to get this unblocked."

# ============================================================================
# CSS DESIGN SYSTEM (Apple/Vercel "Glass" Aesthetic)
# ============================================================================

_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
    :root {
        --bg-absolute: #F4F4F5; --bg-card: rgba(255, 255, 255, 0.75); --bg-glass: rgba(255, 255, 255, 0.6); --bg-elevated: rgba(255, 255, 255, 0.9);
        --graphite-900: #0A0A0A; --graphite-800: #18181B; --graphite-700: #27272A; --graphite-600: #3F3F46; --graphite-500: #71717A; --graphite-400: #A1A1AA; --graphite-300: #D4D4D8; --graphite-200: #E4E4E7; --graphite-100: #F4F4F5;
        --border-light: rgba(10, 10, 10, 0.08); --border-medium: rgba(10, 10, 10, 0.12);
        --shadow-sm: 0 1px 3px rgba(10, 10, 10, 0.05), 0 1px 2px rgba(10, 10, 10, 0.03); --shadow-md: 0 4px 6px rgba(10, 10, 10, 0.05), 0 2px 4px rgba(10, 10, 10, 0.04); --shadow-lg: 0 10px 15px rgba(10, 10, 10, 0.08), 0 4px 6px rgba(10, 10, 10, 0.05);
        --radius-xl: 20px; --radius-lg: 14px; --radius-md: 10px; --radius-sm: 6px; --radius-pill: 9999px;
        --rose: #F43F5E; --rose-softer: rgba(244, 63, 94, 0.05); --amber: #F59E0B; --amber-softer: rgba(245, 158, 11, 0.05); --sky: #0EA5E9; --sky-softer: rgba(14, 165, 233, 0.05); --emerald: #10B981;
    }
    .stApp { background-color: var(--bg-absolute); background-image: radial-gradient(circle at 100% 0%, rgba(14, 165, 233, 0.08) 0%, transparent 25%), radial-gradient(circle at 0% 100%, rgba(124, 58, 237, 0.08) 0%, transparent 25%); color: var(--graphite-900); font-family: 'Inter', -apple-system, sans-serif !important; -webkit-font-smoothing: antialiased; }
    #MainMenu, footer, .stDeployButton, .stAppViewBlockContainer { visibility: hidden !important; display: none !important; }
    .block-container { max-width: 1400px; padding: 2.5rem 3rem 6rem 3rem !important; }
    
    /* Glassmorphism Cards */
    .glass-card { 
        background: var(--bg-card); 
        backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); 
        border: 1px solid var(--border-light); 
        border-radius: var(--radius-xl); padding: 28px; margin-bottom: 24px; 
        box-shadow: var(--shadow-md); position: relative; overflow: hidden; 
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); 
    }
    .glass-card:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); border-color: var(--border-medium); }
    
    h1, h2, h3, h4, h5, h6 { font-family: 'Sora', sans-serif !important; color: var(--graphite-900) !important; letter-spacing: -0.02em !important; line-height: 1.2 !important; }
    h1 { font-size: 3rem !important; font-weight: 600 !important; margin: 0 !important; }
    h1 em { font-style: normal !important; font-weight: 400 !important; color: var(--graphite-500); }
    h2 { font-size: 1.75rem !important; font-weight: 600 !important; }
    h3 { font-size: 1.2rem !important; font-weight: 500 !important; }
    h4 { font-family: 'JetBrains Mono', monospace !important; font-size: 0.75rem !important; text-transform: uppercase; letter-spacing: 0.1em !important; color: var(--graphite-500) !important; font-weight: 500 !important; }
    p, li, span, div { font-family: 'Inter', sans-serif; color: var(--graphite-700); line-height: 1.6; font-size: 0.95rem; }
    strong { color: var(--graphite-900); font-weight: 600; }
    code { font-family: 'JetBrains Mono', monospace !important; background: rgba(10, 10, 10, 0.05) !important; color: var(--graphite-900) !important; padding: 2px 6px; border-radius: 4px; font-size: 0.85em; font-weight: 500; }
    
    .pixel-badge { font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; padding: 5px 12px; border-radius: var(--radius-pill); display: inline-flex; align-items: center; gap: 6px; border: 1px solid var(--border-light); background: var(--bg-elevated); color: var(--graphite-700); }
    .status-dot { width: 6px; height: 6px; border-radius: 50%; display: inline-block; background: var(--graphite-900); animation: pulse-anim 2s cubic-bezier(0.4, 0, 0.2, 1) infinite; }
    @keyframes pulse-anim { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.5; transform: scale(0.8); } }
    
    .stTextInput>div>div>input, .stTextArea textarea, .stSelectbox>div>div, .stRadio>div { background: var(--bg-elevated) !important; border: 1px solid var(--border-light) !important; color: var(--graphite-900) !important; border-radius: var(--radius-md) !important; font-family: 'Inter', sans-serif !important; padding: 12px !important; box-shadow: var(--shadow-sm); transition: all 0.2s ease; }
    .stTextArea textarea { font-family: 'JetBrains Mono', monospace !important; font-size: 0.85rem !important; line-height: 1.6 !important; }
    .stTextInput>div>div>input:focus, .stTextArea textarea:focus { border-color: var(--graphite-900) !important; box-shadow: 0 0 0 3px rgba(10, 10, 10, 0.05) !important; background: white !important; }
    
    /* FIX: Bubble UI for Buttons */
    .stButton>button, .stDownloadButton>button {
        background-color: #FFFFFF !important; 
        color: #0A0A0A !important; 
        font-family: 'Sora', sans-serif !important; 
        font-weight: 600 !important; 
        font-size: 0.9rem !important; 
        border: 1px solid rgba(10, 10, 10, 0.1) !important; 
        border-radius: 9999px !important; 
        padding: 8px 18px !important; 
        width: 100% !important; 
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important; 
        transition: all 0.3s ease !important; 
    }
    .stButton>button:hover, .stDownloadButton>button:hover { 
        background-color: #F4F4F5 !important; 
        border-color: rgba(10, 10, 10, 0.2) !important; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important; 
        transform: translateY(-1px) !important; 
    }
    
    .stTabs [data-baseweb="tab-list"] { gap: 32px; border-bottom: 1px solid var(--border-light); margin-bottom: 32px; background: transparent; }
    .stTabs [data-baseweb="tab"] { font-family: 'Sora', sans-serif !important; font-weight: 500; font-size: 1.1rem; color: var(--graphite-400); padding: 10px 0 14px 0; transition: all 0.2s ease; background: transparent; }
    .stTabs [data-baseweb="tab"]:hover { color: var(--graphite-700); }
    .stTabs [aria-selected="true"] { color: var(--graphite-900) !important; border-bottom: 2px solid var(--graphite-900) !important; }
    
    /* Native Sidebar Support */
    section[data-testid="stSidebar"] { background: var(--bg-glass); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-right: 1px solid var(--border-light); padding: 2rem 1.5rem; }
    section[data-testid="stSidebar"] > div { position: sticky; top: 2rem; }
    section[data-testid="stSidebar"] h3 { font-size: 1rem !important; margin-top: 1.5rem !important; margin-bottom: 0.5rem !important; }
    section[data-testid="stSidebar"] label { font-family: 'JetBrains Mono', monospace !important; font-size: 0.7rem !important; text-transform: uppercase; letter-spacing: 0.1em; color: var(--graphite-500) !important; }
    
    /* Commitment Rows */
    .commitment-row { padding: 16px; border-radius: var(--radius-md); margin-bottom: 12px; border: 1px solid var(--border-light); transition: all 0.2s ease; }
    .commitment-row:hover { transform: translateX(4px); box-shadow: var(--shadow-md); }
    .row-top { display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px; }
    .row-left { display: flex; align-items: center; gap: 10px; }
    .commitment-text { font-family: 'Inter', sans-serif; font-size: 0.95rem; color: var(--graphite-900); font-weight: 500; }
    .stall-score { font-family: 'JetBrains Mono', monospace; font-size: 1.2rem; font-weight: 700; }
    .row-bottom { display: flex; gap: 16px; font-size: 0.8rem; color: var(--graphite-600); font-family: 'JetBrains Mono', monospace; flex-wrap: wrap; }
    
    .stProgress > div > div > div > div { background: var(--graphite-900) !important; }
    .stSpinner > div > div { border-top-color: var(--graphite-900) !important; }
</style>
"""

# ============================================================================
# INTERACTIVE PARTICLE CANVAS (Subtle Ambient Physics)
# ============================================================================

_PARTICLE_CANVAS = """
<div style="position: relative; height: 280px; border-radius: 20px; overflow: hidden; border: 1px solid rgba(10,10,10,0.05); background: rgba(255,255,255,0.5); backdrop-filter: blur(10px); box-shadow: 0 10px 20px rgba(10,10,10,0.03); margin-bottom: 32px;">
    <canvas id="glassCanvas" style="position: absolute; inset: 0; width: 100%; height: 100%;"></canvas>
    <div style="position: absolute; top: 32px; left: 40px; z-index: 10; pointer-events: none;">
        <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 6px;">
            <div style="width: 6px; height: 6px; background: #0A0A0A; border-radius: 50%;"></div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 10px; font-weight: 600; letter-spacing: 0.1em; color: #0A0A0A; text-transform: uppercase;">Universal Engine</span>
        </div>
        <div style="font-family: 'Sora', sans-serif; font-size: 32px; font-weight: 600; color: #0A0A0A; letter-spacing: -0.02em;">Commitment Integrity OS</div>
        <div style="font-family: 'Inter', sans-serif; font-size: 13px; color: #71717A; margin-top: 2px;">Tracking every promise, across every domain.</div>
    </div>
</div>
<script>
const canvas = document.getElementById('glassCanvas');
const ctx = canvas.getContext('2d');
let width, height, particles = [];
const SPACING = 40; let time = 0;
function initCanvas() {
    width = canvas.width = canvas.offsetWidth * window.devicePixelRatio;
    height = canvas.height = canvas.offsetHeight * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    width = canvas.offsetWidth; height = canvas.offsetHeight;
    particles = [];
    for (let x = -width * 0.6; x < width * 1.6; x += SPACING) {
        for (let y = -height * 0.6; y < height * 1.6; y += SPACING) {
            if (Math.random() > 0.4) continue;
            particles.push({ ox: x, oy: y, cx: x, cy: y, vx: 0, vy: 0, size: Math.random() * 2 + 1 });
        }
    }
}
window.addEventListener('resize', initCanvas); initCanvas();
let mouse = { x: -1000, y: -1000, radius: 150 };
canvas.addEventListener('mousemove', (e) => { const rect = canvas.getBoundingClientRect(); mouse.x = e.clientX - rect.left; mouse.y = e.clientY - rect.top; });
canvas.addEventListener('mouseleave', () => { mouse.x = -1000; mouse.y = -1000; });
function animate() {
    ctx.clearRect(0, 0, width, height); time += 0.005;
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        const z = Math.sin(p.ox * 0.005 + time) * Math.cos(p.oy * 0.005 + time) * 15;
        const targetX = (p.ox - p.oy) * 0.6 + width / 2;
        const targetY = (p.ox + p.oy) * 0.3 + z + height / 2;
        const dx = p.cx - mouse.x, dy = p.cy - mouse.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) { const force = (mouse.radius - dist) / mouse.radius; p.vx += (dx / dist) * force * 2; p.vy += (dy / dist) * force * 2; }
        p.vx += (targetX - p.cx) * 0.03; p.vy += (targetY - p.cy) * 0.03; p.vx *= 0.9; p.vy *= 0.9; p.cx += p.vx; p.cy += p.vy;
        
        for (let j = i + 1; j < particles.length; j++) {
            const p2 = particles[j];
            const ddx = p.cx - p2.cx, ddy = p.cy - p2.cy;
            const ddist = Math.sqrt(ddx * ddx + ddy * ddy);
            if (ddist < 100 && ddist > 0) {
                const opacity = 1 - (ddist / 100);
                ctx.beginPath(); ctx.moveTo(p.cx, p.cy); ctx.lineTo(p2.cx, p2.cy);
                ctx.strokeStyle = 'rgba(10, 10, 10, ' + (opacity * 0.15) + ')'; ctx.lineWidth = 0.5; ctx.stroke();
            }
        }
        if (p.cx > -30 && p.cx < width + 30 && p.cy > -30 && p.cy < height + 30) { ctx.fillStyle = 'rgba(10, 10, 10, 0.4)'; ctx.fillRect(p.cx - p.size / 2, p.cy - p.size / 2, p.size, p.size); }
    }
    requestAnimationFrame(animate);
}
animate();
</script>
"""

# ============================================================================
# MAIN STREAMLIT APPLICATION
# ============================================================================

def render_header():
    st.markdown(_h("""
    <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 32px;">
        <div>
            <h1>Just tell me <em>what's stalled.</em></h1>
            <div style="font-family: 'JetBrains Mono', monospace; font-size: 12px; color: var(--graphite-500); margin-top: 10px;">synthesis is automation, judgment is yours_</div>
        </div>
        <div style="text-align: right;">
            <span class="pixel-badge"><span class="status-dot"></span>ONLINE</span>
        </div>
    </div>
    """), unsafe_allow_html=True)

def render_sidebar():
    with st.sidebar:
        st.markdown('<span class="pixel-badge">CONTROL</span>', unsafe_allow_html=True)
        st.markdown("#### Industry Filter")
        industry_filter = st.selectbox("Filter by Domain", ["All"] + INDUSTRIES, index=0)
        st.markdown("---")
        st.markdown("#### Log New Commitment")
        
        with st.form("add_commitment_form"):
            c_industry = st.selectbox("Industry", INDUSTRIES)
            c_text = st.text_input("Commitment Text (What was promised?)")
            c_owner = st.text_input("Owner Name")
            c_exp = st.number_input("Expected Minutes", min_value=10, max_value=10080, value=120)
            c_sev = st.selectbox("Severity", ["low", "medium", "high", "critical"])
            c_rel = st.slider("Owner Reliability (0-1)", 0.0, 1.0, 0.85, 0.05)
            c_blast = st.selectbox("Blast Radius", ["Isolated", "Multi-Team", "Critical Path"])
            c_art = st.text_input("Expected Artifact (e.g., 'Lab Report', 'PR Review')")
            c_dep = st.text_input("Dependency (e.g., 'QA Team', 'None')")
            submitted = st.form_submit_button("Log Commitment")
            
            if submitted and c_text and c_owner:
                cid = hashlib.md5(f"{c_industry}:{c_text}:{uuid.uuid4()}".encode()).hexdigest()[:12]
                promised = datetime.now().isoformat()
                with _db() as conn:
                    conn.execute("INSERT INTO commitments VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                                 (cid, c_industry, c_text, c_owner, promised, c_exp, c_sev, c_rel, c_blast, c_art, c_dep, "Open"))
                    conn.commit()
                st.success("Commitment Logged!")
                time.sleep(1)
                st.rerun()

    return industry_filter

def render_ledger_tab(industry_filter: str):
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(_h("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
            <h3 style="margin: 0;">Universal Commitment Ledger</h3>
            <p style="margin: 6px 0 0; font-size: 0.85rem; color: var(--graphite-500);">Live stall scores, sorted by risk. Click to generate empathetic nudges.</p>
        </div>
    </div>
    """), unsafe_allow_html=True)
    
    commitments = load_commitments(industry_filter)
    commitments.sort(key=lambda x: x.stall_score, reverse=True)
    
    for c in commitments:
        st.markdown(_h(c.to_html_row()), unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 4])
        with col1:
            if st.button("Resolve", key=f"res_{c.id}"):
                update_commitment_status(c.id, "Resolved")
                st.rerun()
        with col2:
            if st.button("Generate Nudge", key=f"nud_{c.id}"):
                st.session_state['nudge_target'] = c.id
                st.rerun()
        with col3:
            if st.session_state.get('nudge_target') == c.id:
                with st.spinner("Drafting empathetic nudge..."):
                    nudge = generate_nudge(c)
                st.info(nudge)
    
    st.markdown("</div>", unsafe_allow_html=True)

def render_brief_tab(industry_filter: str):
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown(_h("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
            <h3 style="margin: 0;">Pod Action Brief</h3>
            <p style="margin: 6px 0 0; font-size: 0.85rem; color: var(--graphite-500);">Generated by the Human Tone Engine.</p>
        </div>
        <span class="pixel-badge">AI SYNTHESIS</span>
    </div>
    """), unsafe_allow_html=True)
    
    commitments = load_commitments(industry_filter)
    
    if st.button("Generate Morning Brief", use_container_width=True):
        with st.spinner("Synthesizing operational reality..."):
            brief = generate_pod_action_brief(commitments)
        st.markdown(brief)
    
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title=f"{APP_NAME} :: {APP_TAGLINE}", page_icon="|", layout="wide", initial_sidebar_state="expanded", menu_items={"About": f"# {APP_NAME} v{APP_VERSION}\n{APP_TAGLINE}"})
    _db().close() # Ensure DB exists and seeds
    st.markdown(_CSS, unsafe_allow_html=True)
    render_header()
    components.html(_PARTICLE_CANVAS, height=292)
    
    industry_filter = render_sidebar()
    
    tab_ledger, tab_brief = st.tabs(["Commitment Ledger", "Pod Action Brief"])
    with tab_ledger: render_ledger_tab(industry_filter)
    with tab_brief: render_brief_tab(industry_filter)

if __name__ == "__main__":
    main()