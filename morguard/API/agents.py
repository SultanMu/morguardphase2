async def get_query(folder_name: str):
    if folder_name == "Energy - Water Audit":
        queries = """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it in about 400 words
        3. summarise the "Summary" at the goal 1 and the summary at goal 2 above

        Example of summary at goal 1:
        wewere hired on behalf of Morguard Investments Ltd., to conduct a Level 1 Walkthrough Energy & Water Audit Report of Place Rosemère, located at 401 Boulevard Labelle in Rosemère, Québec. The assessment was performed as an environmental best practice, in accordance with the Building Owners and Managers Association’s Building Environmental Standards (BOMA BEST®) program. In accordance with BOMA BEST® standards, the objective of this report is to provide a:
        • Utility and water billing analysis with benchmarking observations, based on a minimum of 12 months of continuous billing data (no older than 18 months),
        • Summary of major energy-consuming equipment (i.e., types of lighting and mechanical equipment),
        • Summary of current water-consuming systems in the building,
        • List of proposed low-cost energy and water conservation measures, estimated savings, and simple payback (i.e., Energy and Water Management Plans),
        • Reporting requirements for energy and water benchmarking, in accordance with BOMA BEST® standards (and provincial regulations, where applicable).
        The walkthrough audit was conducted by Ms. Nichole Bonner; Senior Manager, Sustainability Services and Ms. Chelsey DiManno; Senior Specialist, Sustainability Services of CD SONTER Ltd. on April 12 and 13, 2017. In conjunction with the facility walkthrough, interviews were conducted with site operating personnel including Mr. Brian Deslauriers, Directeur des Opérations and Mr. Christian Larivière, Superviseur des Opèrations. Mr. Deslauriers and Mr. Larivière provided documented information on utility consumption for the audit period: January 1, 2014 to December 31, 2016. The scope of the walkthrough was limited to the common and service areas of the building, comprising approximately 186,825 square feet (sq. ft.), as well as building exterior landscaped and parking areas.
        The 2016 annual utility consumption for the building includes approximately:
        • 19,283,315 kilowatt hours (kWh) of electricity consumed in building exterior areas, common and service areas, all non-anchor tenant leased areas, and one (1) anchor tenant leased area (a total of 808,327 sq. ft.). This total equates to approximately 23.9 kWh/sq. ft./year.
        • 77,672 cubic meters (m3) of natural gas consumed in common and service areas, most non-anchor tenant leased areas, and one (1) anchor tenant leased area (a total of 779,771 sq. ft.). This total equates to approximately 0.1 m3/sq. ft./year.
        • 52,519 m3 of water consumed in building exterior areas, common and service areas, all non-anchor tenant leased areas, and one (1) anchor tenant leased area (an approximate total of 814,341 sq. ft.). This total equates to approximately 0.06 m3/sq. ft./year.
        The 2016 annual utility costs for the building include approximately:
        • $1,706,715.89 for electricity consumed in building exterior areas, common and service areas, all non-anchor tenant leased areas, and one (1) anchor tenant leased area. This total equates to approximately $2.11/sq. ft./year.
        • $39,365.99 for natural gas consumed in common and service areas, most non-anchor tenant leased areas, and one (1) anchor tenant leased area. This total equates to approximately $0.05/sq. ft./year.
        • $41,055.48 for water consumed in building exterior areas, common and service areas, all non-anchor tenant leased areas, and one (1) anchor tenant leased area. This total equates to approximately $0.05/sq. ft./year.

        Example of summary output required:
        The Level 1 Walkthrough Energy & Water Audit Report was conducted at Place Rosemère, located in Rosemère, Québec. The audit included utility and water billing analysis, major energy-consuming equipment summary, current water-consuming systems summary, proposed energy and water conservation measures, and reporting requirements. The audit was performed by CD SONTER Ltd. on April 12 and 13, 2017, with interviews conducted with site operating personnel. The annual utility consumption and costs for 2016 were detailed for electricity, natural gas, and water.

        Output:
        Return all the data as valid JSON
        """ 
        # queries = [query1, query2, query3, query4, query5, query6, query7]

    elif folder_name == "Property Condition Assessments":
        queries = """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it
        3. summarise the "Summary" at the step 1 and the summary at step 2 above

        Output:
        return all these fields as valid JSON
        """ 
    elif folder_name == "Energy and Water Management Plans":
        queries= """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it
        3. summarise the "Summary" at the step 1 and the summary at step 2 above

        Output:
        return all these fields as valid JSON  
        """ 

    elif folder_name == "Emergency Preparedness Plans":
        queries= """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it
        3. summarise the "Summary" at the step 1 and the summary at step 2 above

        Output:
        return all these fields as valid JSON   
        """ 

    elif folder_name == "IAQ Audit":
        queries= """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it
        3. summarise the "Summary" at the step 1 and the summary at step 2 above

        Output:
        return all these fields as valid JSON  
        """ 
    elif folder_name == "Waste Audit":
        queries= """ 
        Objective: 
        You are an expert in reading pdf files. Your objective is to scrap data from the document. 
        look for the following in the document:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"

        Goals:
        1. the goal is it properly scrap the folloing fields from the document
        fields:
        "Report Type"
        "Report Title"
        "Date Created"
        "Next assessment date"
        "Company"
        "Author"
        "Summary"
        2. read the entire document and summarise it
        3. summarise the "Summary" at the step 1 and the summary at step 2 above

        Output:
        return all these fields as valid JSON  
        """ 
    else:
        queries = []  

    return queries
