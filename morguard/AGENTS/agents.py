import os
import openai

class BaseLLaMAAgent:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def generate_text_with_prompt(self, prompt):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0]["text"]

class EmergencyPreparednessPlansAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Emergency Preparedness Plans based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class EnergyAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Energy Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class WaterAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Water Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class EnergyAndWaterAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Energy and Water Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class EnergyManagementPlanAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Energy Management Plan based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class WaterManagementPlanAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Water Management Plan based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class EnergyAndWaterManagementPlanAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Energy and Water Management Plan based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class IAQAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for IAQ Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class PropertyConditionAssessmentsAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Property Condition Assessments based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class WasteAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Waste Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)

class CanadianCertifiedRentalBuildingProgramAuditAgent(BaseLLaMAAgent):
    def process_request(self, request_data):
        prompt = f"Your custom prompt for Canadian Certified Rental Building Program Audit based on: {request_data}"
        return self.generate_text_with_prompt(prompt)
