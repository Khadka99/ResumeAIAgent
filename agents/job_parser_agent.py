data = parse_json(json_text)

return JobRequirements.model_validate(data)