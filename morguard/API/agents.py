async def get_query(folder_name: str):
    if folder_name == "Energy - Water Audit":
        queries = [
            """
            You are extracting data from an "Energy - Water Audit" report. 

            Query: Extract the "Report Type" from the document. This refers to the specific classification or category of the report, indicating it belongs to an "Energy - Water Audit" type. Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to energy-water audit and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return the result as a valid json: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Extract the "Date Created" from the document. This is the date on which the report was originally created or published. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Extract the "Next Assessment Date" from the document. This date indicates when the next scheduled assessment or audit is due. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Extract the "Company" name from the document. This refers to the organization or entity that conducted the audit or is responsible for the report. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the individual or group of individuals responsible for writing the report. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from an "Energy - Water Audit" report.

            Query: Extract the "Summary" of the report from the document. The summary provides a brief overview of the key findings, objectives, or conclusions of the report. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    elif folder_name == "Property Condition Assessments":
        queries = [
            """
            You are extracting data from a "Property Condition Assessment" report. 

            Query: Extract the "Report Type" from the document. This indicates the category of the report, which is a "Property Condition Assessment". Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to property condition assessment and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return the result as a valid json: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Extract the "Date Created" from the document. This date reflects when the report was written or finalized. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Extract the "Next Assessment Date" from the document. This date suggests when the following assessment should be performed. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Extract the "Company" name from the document. This is the organization that prepared or commissioned the report. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the person or persons responsible for writing creating the report. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from a "Property Condition Assessment" report.

            Query: Extract the "Summary" of the report from the document. This summary provides an overview of the assessment's findings, recommendations, and conclusions. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    elif folder_name == "Energy and Water Management Plans":
        queries = [
            """
            You are extracting data from an "Energy and Water Management Plan" report. 

            Query: Extract the "Report Type" from the document. This identifies the document as an "Energy and Water Management Plan". Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to energy and water management plans and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return the result as a valid json: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Extract the "Date Created" from the document. This date represents when the plan was documented or approved. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Extract the "Next Assessment Date" from the document. This date signifies when the next review or assessment of the plan is scheduled. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Extract the "Company" name from the document. This is the company responsible for creating or implementing the management plan. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the person or group responsible for writing the management plan. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from an "Energy and Water Management Plan" report.

            Query: Extract the "Summary" of the report from the document. The summary provides an overview of the goals, strategies, and outcomes of the management plan. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    elif folder_name == "Emergency Preparedness Plans":
        queries = [
            """
            You are extracting data from an "Emergency Preparedness Plan" report. 

            Query: Extract the "Report Type" from the document. This label indicates that the document is an "Emergency Preparedness Plan". Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to emergency preparedness plans and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Extract the "Date Created" from the document. This is the date when the preparedness plan was created or finalized. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Extract the "Next Assessment Date" from the document. This date indicates when the next review or update of the plan is due. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Extract the "Company" name from the document. This refers to the organization that prepared the emergency preparedness plan. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the person or team responsible for writing the emergency plan. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from an "Emergency Preparedness Plan" report.

            Query: Extract the "Summary" of the report from the document. The summary provides an overview of the plan's key points, objectives, and strategies for emergency preparedness. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    elif folder_name == "IAQ Audit":
        queries = [
            """
            You are extracting data from an "IAQ Audit" report. 

            Query: Extract the "Report Type" from the document. This label indicates that the document is an "Indoor Air Quality (IAQ) Audit" report. Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to IAQ Audit and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Extract the "Date Created" from the document. This date represents when the IAQ audit report was generated. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Extract the "Next Assessment Date" from the document. This is the date when the next IAQ audit is scheduled. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Extract the "Company" name from the document. This refers to the company that conducted the IAQ audit. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the individual or team responsible for writing the IAQ audit report. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from an "IAQ Audit" report.

            Query: Extract the "Summary" of the report from the document. The summary should provide an overview of the key findings, conclusions, and recommendations of the IAQ audit. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    elif folder_name == "Waste Audit":
        queries = [
            """
            You are extracting data from a "Waste Audit" report. 

            Query: Extract the "Report Type" from the document. This indicates the document is a "Waste Audit" report, identifying the category and focus of the content. Return only the result in the following JSON format: {"Report Type": "[Report Type]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Identify and extract the "Report Title" from the document. Ensure the title is relevant to Waste Audit and not a file name or unrelated heading. If the title is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Report Title": "[Report Title]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Extract the "Date Created" from the document. This is the date when the waste audit report was written or published. If the "Date Created" is missing or unclear, return "Not Available". Return only the result in the following JSON format: {"Date Created": "[Date]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Extract the "Next Assessment Date" from the document. This date indicates when the next waste audit is planned. If not found, return "Not Available". Return only the result in the following JSON format: {"Next Assessment Date": "[Next Assessment Date]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Extract the "Company" name from the document. This refers to the organization responsible for conducting the waste audit. If not found, return "Not Available". Return only the result in the following JSON format: {"Company": "[Company]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Extract the "Author" of the report from the document. Avoid using the name of the document or any text editor name like MS word. This is the person or team responsible for writing the waste audit report. If not found, return "Not Available". Return only the result in the following JSON format: {"Author": "[Author]"}
            """,
            """
            You are extracting data from a "Waste Audit" report.

            Query: Extract the "Summary" of the report from the document. The summary should provide a concise overview of the waste audit's findings, recommendations, and conclusions. If a summary is not explicitly labeled, create a concise summary based on the content. Return only the result in the following JSON format: {"Summary": "[Summary]"}
            """
        ]

    else:
        queries = []

    return queries
