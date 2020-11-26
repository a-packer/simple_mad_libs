"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


story2 = Story(
    ["adjective", "noun", "number", "plural_noun", "ing_verb"],
    """You're a {adjective} {noun} with {number} {plural_noun} and you rock at {ing_verb}!"""
)

story3 = Story(
    ["verb", "plural_noun", "adjective", "noun"],
    """Remember to {verb} with {plural_noun} and be a {adjective} {noun}."""
)

story4 = Story(
    ["noun", "adverb", "verb", "plural_noun"],
    """In the near future, a {noun} will {adverb} {verb} on all of your {plural_noun}"""
)

# Make dict of {code:story, code:story, ...}
stories = [story1, story2, story3, story4]
