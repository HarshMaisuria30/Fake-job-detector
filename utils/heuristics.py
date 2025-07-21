# =========================================
# Fake Job Detector Project
# Author: Harsh Maisuria
# Year: 2025
# Description: Streamlit-based web app to detect fake job postings
# =========================================


def is_suspect_job(description: str, requirements: str) -> bool:
    text = (description + ' ' + requirements).lower()

    scam_keywords = [
        'investment', 'bitcoin', 'send money', 'click here',
        'urgent requirement', 'no experience', 'quick money',
        'wire funds', 'work from home and earn', 'transfer money'
    ]
    keyword_hits = sum(1 for word in scam_keywords if word in text)

    if len(description.split()) < 10:
        return True

    if keyword_hits >= 2:
        return True

    if 'high salary' in text and 'no experience' in text:
        return True

    role_keywords = {
    'software developer': ['python', 'java', 'c++', 'git', 'api', 'algorithms', 'oop', 'debugging'],
    'data analyst': ['excel', 'sql', 'tableau', 'power bi', 'data', 'visualization', 'pivot table', 'statistics', 'python'],
    'web developer': ['html', 'css', 'javascript', 'react', 'frontend', 'backend', 'bootstrap', 'dom'],
    'machine learning engineer': ['machine learning', 'scikit-learn', 'pandas', 'numpy', 'model', 'training', 'overfitting', 'validation'],
    'project manager': ['planning', 'timeline', 'scrum', 'agile', 'project', 'milestones', 'jira', 'stakeholders'],
    'devops engineer': ['docker', 'kubernetes', 'ci/cd', 'linux', 'aws', 'jenkins', 'infrastructure', 'monitoring'],
    'ui ux designer': ['figma', 'adobe xd', 'wireframe', 'prototype', 'user testing', 'design system', 'affinity map'],
    'mobile app developer': ['android', 'kotlin', 'java', 'flutter', 'ios', 'swift', 'react native', 'apk'],
    'backend developer': ['node.js', 'django', 'flask', 'api', 'sql', 'database', 'server', 'express'],
    'frontend developer': ['html', 'css', 'javascript', 'react', 'typescript', 'redux', 'ui', 'components'],
    'full stack developer': ['frontend', 'backend', 'react', 'node.js', 'api', 'database', 'javascript', 'devops'],
    'cybersecurity analyst': ['network', 'firewall', 'encryption', 'penetration testing', 'vulnerability', 'threat', 'ids', 'kali linux'],
    'cloud engineer': ['aws', 'azure', 'gcp', 'cloud', 'deployment', 's3', 'lambda', 'terraform'],
    'business analyst': ['excel', 'sql', 'requirements', 'stakeholders', 'dashboard', 'gap analysis', 'user stories'],
    'qa tester': ['manual testing', 'test case', 'automation', 'selenium', 'bug report', 'regression', 'junit', 'quality assurance'],
    'graphic designer': ['photoshop', 'illustrator', 'figma', 'typography', 'layout', 'color theory', 'branding'],
    'content writer': ['seo', 'grammar', 'writing', 'editing', 'blog', 'keyword', 'tone', 'headlines'],
    'digital marketer': ['seo', 'sem', 'facebook ads', 'google ads', 'analytics', 'campaigns', 'email marketing', 'engagement'],
    'hr executive': ['recruitment', 'interview', 'payroll', 'onboarding', 'policies', 'hrms', 'conflict resolution'],
    'accountant': ['tally', 'gst', 'invoice', 'ledger', 'reconciliation', 'financial statements', 'audit'],
}

    detected_role = None
    for role in role_keywords:
        if role in description.lower():
            detected_role = role
            break

    if detected_role:
        expected_skills = role_keywords[detected_role]
        match_count = sum(1 for skill in expected_skills if skill in requirements.lower())
        if match_count < 3:
            return True, f"{match_count} of {len(expected_skills)} skills match for role: {detected_role.title()}"
        else:
            return False, f"{match_count} of {len(expected_skills)} skills match for role: {detected_role.title()}"


    return False, "No suspicious pattern"

