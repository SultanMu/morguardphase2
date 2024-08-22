async def get_query(folder_name: str):
    if folder_name == "Energy - Water Audit":
        queries = """
        Context:
        You are extracting data from an "Energy - Water Audit" report. These reports typically focus on the assessment of energy and water usage, efficiency, and recommendations for improvement.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    elif folder_name == "Property Condition Assessments":
        queries = """
        Context:
        You are working with a "Property Condition Assessment" report. These reports generally evaluate the physical condition of a property, including structures, systems, and components.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    elif folder_name == "Energy and Water Management Plans":
        queries = """
        Context:
        You are processing an "Energy and Water Management Plan" report. These documents typically outline strategies and recommendations for managing energy and water resources efficiently.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    elif folder_name == "Emergency Preparedness Plans":
        queries = """
        Context:
        You are working with an "Emergency Preparedness Plan" report. These reports are focused on planning and preparing for potential emergencies, including safety protocols and response strategies.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    elif folder_name == "IAQ Audit":
        queries = """
        Context:
        You are working with an "IAQ Audit" (Indoor Air Quality Audit) report. These documents assess the quality of indoor air and provide recommendations for improvement.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    elif folder_name == "Waste Audit":
        queries = """
        Context:
        You are working with a "Waste Audit" report. These reports evaluate waste generation, management practices, and provide recommendations for reducing waste.

        Objective:
        Your task is to extract specific information from the document without generating or inferring any content. If any information is missing or unclear, return "Not Available" instead of guessing or adding irrelevant content. Extract the following fields:
        - "Report Type"
        - "Report Title"
        - "Date Created"
        - "Next Assessment Date"
        - "Company"
        - "Author"
        - "Summary"

        Goals:
        1. Extract only the data explicitly mentioned in the document for each of the specified fields.
        2. Summarize the entire document with a focus on the provided content, avoiding external information or assumptions.
        3. Provide a concise summary of the "Summary" field from goal 1 based on the extracted text.

        Output:
        Return all data as valid JSON. Ensure each field contains only relevant extracted content, with fields not found in the document marked as "Not Available".
        """

    else:
        queries = []

    return queries
