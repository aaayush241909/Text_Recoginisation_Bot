import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
R_JOKE = ['''How do doggy robots do?.........
             They byte!''' ,
            ''' Why don’t pirates take a shower before they walk the plank?
                They just wash up on shore.''',
            ''' Patient: Doctor! You've got to help me! Nobody ever listens to me. No one ever pays any attention to what I have to say.
                Doctor: Next please!''',
            ''' Teacher: Do you have trouble making decisions?
                Student: Well...yes and no.'''][random.randrange(4)]

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response
