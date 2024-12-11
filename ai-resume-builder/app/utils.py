def generate_suggestions(section):
    suggestions_map = {
        "skills": ["Add technical skills relevant to your job.", "Include programming languages and tools."],
        "experience": ["Use action verbs like 'Managed', 'Designed', etc.", "Quantify achievements where possible."],
        "education": ["Mention degrees, certifications, and relevant coursework."]
    }
    return suggestions_map.get(section.lower(), ["No suggestions available."])

def generate_resume(data):
    # Example formatting logic
    resume_template = f"""
    Name: {data['name']}
    Contact: {data['contact']}
    Summary: {data['summary']}
    
    Skills:
    {', '.join(data['skills'])}
    
    Experience:
    {data['experience']}
    
    Education:
    {data['education']}
    """
    return resume_template
