parsing_instructions="""
Document Type: Audit Report

Key Fields to Extract with Relevant Keywords:

Report Title:

Keywords: "Title," "Report Title," or bolded text near the top of the document.
Location: Typically located at the very beginning of the document, often bolded or formatted as a heading.
Date Created:

Keywords: "Date Created," "Issued Date," "Creation Date."
Location: Usually found near the title or in metadata sections, headers, or footers.
Next Assessment Date:

Keywords: "Next Assessment Date," "Next Review Date," "Review Cycle," "Scheduled Review."
Location: May be located in sections like the summary, conclusion, or validity statements.
Author:

Keywords: "Author," "Prepared by," "Report Author," "Prepared for."
Location: Typically found near the title, in footers, or in the signature section of the document.
Summary:

Keywords: "Executive Summary," "Summary," "Key Findings," "Overview."
Location: Usually appears in a "Summary" or "Executive Summary" section or can be inferred from the introduction or conclusion.
"""
query="""
Extract the following from the and return the result in valid JSON format:

1. Report Title: What is the "Report Title" of the document/report? If not found in the document, use the file name. If no "Title" is found, return "Not Available".  

2. Date Created: What is the Date the document was created? It is generally found on the first page and may be listed as "Date prepared." If not found, use the file creation date. Provide the result in YYYY-MM-DD or YYYY-MM format if the day is unavailable. If none is found, return "Not Available".  

3. Next Assessment Date: What is the "Next Assessment Date"? Present it in YYYY-MM-DD or YYYY-MM format if the day is not found. If missing, calculate it by adding three months to the "Date Created".  

4. Company: Find the name of the "Company" or organization that prepared the document/report. It may appear as "Préparé par" or "prepared by". Avoid the client company name and prioritize the company that prepared the document. Extract from the document or file name if needed. If unavailable, return "Not Available".  

5. Author: Extract the "Author" of the document, look for terms such as "author", "prepared by", or "submitted by". The author may be the person who signed the document. If unavailable, return "Not Available".  

6. Summary: Summarize the executive summary, if present, then summarize the entire document/report in 180-200 words, including important facts and figures.  

"""