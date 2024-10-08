parsing_instructions="""
The task is to extract specific information from a document, typically a report such as an audit or similar structured document. The extracted data will be used for further processing and analysis, so precision and structured output are essential. The extraction process involves identifying relevant sections or metadata that may contain the required information. When explicit data is not available, predefined fallback strategies must be applied, such as using file metadata or performing simple calculations.

Key elements of the document to be parsed include the title, dates, author information, company name, and summaries of the content. These elements are often formatted in predictable ways, such as headings, dates, or specific keywords like "Prepared by" or "Date Created". The document may use various terminologies or formats, so the parser must be flexible enough to account for different layouts and wordings. In cases where the required information is missing, fallback methods, such as deriving data from the document's metadata or calculating estimates, will be applied.

The output must be structured in a valid and machine-readable format, ensuring consistency across documents regardless of minor variations in structure or formatting."""
query="""
Extract the following information from the document and return the result in valid JSON format:

Report Title:

Identify the "Report Title" of the document. If a title is not found, use the file name. If neither is available, return "Not Available."
Date Created:

Extract the date the document was created, generally found on the first page and may be labeled as "Date Prepared." If not found in the document, use the file creation date. Return the result in YYYY-MM-DD format, or YYYY-MM if the exact day is unavailable. If no date is found, return "Not Available."
Next Assessment Date:

Locate the "Next Assessment Date." If unavailable, calculate it by adding three months to the "Date Created" and provide the result in YYYY-MM-DD or YYYY-MM format if the day is unavailable. If no "Date Created" is available to calculate from, return "Not Available."
Company:

Extract the name of the company or organization that prepared the document. Look for labels such as "Prepared by" or "Préparé par." If the company name cannot be found, use the file name if it contains relevant information. If still unavailable, return "Not Available."
Author:

Find the name of the document's author. Look for terms such as "Author," "Prepared by," or "Submitted by." If the author is not found, return "Not Available."
Summary:

Extract and summarize the executive summary, if present. If there is no executive summary, provide a concise summary of the document in 180-200 words, including key facts and figures.

"""