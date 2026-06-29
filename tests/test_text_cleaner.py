from narratorpro.core.text_cleaner import clean
def test_clean():
    assert clean("A   B")=="A B"
