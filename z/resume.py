from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.set_text_color(30, 30, 30)
        self.cell(0, 10, "ASHOK KUMAR", ln=True, align="C")

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, title, ln=True)
        self.ln(1)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Contact Information
pdf.set_font("Arial", "", 11)
pdf.multi_cell(0, 8, "Phone: 9540379752 | Email: ajaibind@gmail.com")
pdf.multi_cell(0, 8, "Address: 195, Jai Shankar Verma Marg, South Extension I, Aliganj, Kotla Mubarakpur, Sewa Nagar, New Delhi, Delhi 110003")
pdf.ln(5)

# Objective
pdf.chapter_title("OBJECTIVE")
pdf.chapter_body("Experienced and detail-oriented Sound Engineer and Installer with 15+ years of expertise in live sound handling, audio system installation, and technical support across India. Known for delivering reliable setups for schools, auditoriums, and corporate events with precision and professionalism.")

# Experience
pdf.chapter_title("PROFESSIONAL EXPERIENCE")
pdf.chapter_body("Sound Engineer – Modern Stage Service, Delhi (2008 – Present)\n- Managed live sound operations for concerts, conferences, and social events.\n- Operated analog/digital mixers, microphones, and full-range speaker systems.\n- Led a team of assistants and ensured flawless execution during live performances.\n- Conducted equipment checks, fault diagnosis, and timely resolutions.")

pdf.chapter_body("Installer – Delhi Public School & Pan-India Sound Projects (Ongoing)\n- Installed complete sound systems in schools, auditoriums, and halls across India.\n- Worked on long-term audio setup projects for Delhi Public School.\n- Configured mixers, amplifiers, PA systems, and acoustics with precision.\n- Delivered post-installation training and support for local operators.")

# Skills
pdf.chapter_title("KEY SKILLS")
skills = [
    "Live Sound Mixing & Monitoring",
    "PA System & Speaker Setup",
    "Audio Installation (Schools, Auditoriums, Events)",
    "Digital/Analog Mixer Operation",
    "All-India Project Execution",
    "Team Supervision & Technical Support"
]
pdf.chapter_body('\n'.join(skills))

# Education
pdf.chapter_title("EDUCATION")
pdf.chapter_body("10th – UP Board")

# Personal
pdf.chapter_title("PERSONAL DETAILS")
pdf.chapter_body(
    "Father’s Name: Baliram\nDate of Birth: 01 May 1987\nGender: Male\nNationality: Indian\nLanguages Known: Hindi"
)

# Save PDF
pdf.output("Ashok_Kumar_Resume.pdf")
