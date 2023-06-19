import cohere
import config

def generate_recipe(form_data):
    api_token = config.COHERE_TOKEN
    co = cohere.Client(api_token)
    prompt = f"Find a {form_data['SelectedMeal']} recipe with: {form_data['Food']}, roughly {form_data['Calories']} calories, from {form_data['Culture']} culture. The format should be \nName: \n\nIngredients: \nSteps:. Do not say anything else, Make sure the steps are numbered, include calories and macronutrients."
    response = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=1000,
        temperature=2,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE'
    )
    recipe = response.generations[0].text
    return recipe
