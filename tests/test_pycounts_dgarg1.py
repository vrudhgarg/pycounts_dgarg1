# from pycounts_dgarg1.gg import count_words
import pycounts_dgarg1 as pdgarg1
from collections import Counter
from pycounts_dgarg1.plotting import plot_words 
import matplotlib    
import pytest

@pytest.fixture         
def einstein_counts(): 
    return Counter({'insanity': 1, 'is': 1, 'doing': 1, 
                    'the': 1, 'same': 1, 'thing': 1, 
                    'over': 2, 'and': 2, 'expecting': 1,
                    'different': 1, 'results': 1})

def test_count_words(einstein_counts):  
    """Test word counting from a file."""
    expected = einstein_counts
    actual = pdgarg1.count_words("tests/einstein.txt")
    assert actual == expected, "Einstein quote counted incorrectly!"

def test_plot_words(einstein_counts):   
    """Test plotting of word counts."""
    fig = plot_words(einstein_counts)
    assert isinstance(fig, matplotlib.container.BarContainer), \
           "Wrong plot type"
    assert len(fig.datavalues) == 10, "Incorrect number of bars plotted"
    

def test_plot_words_error(): 
    """Check TypeError raised when Counter not used."""
    with pytest.raises(TypeError):
        list_object = ["Pythons", "are", "non", "venomous"]
        plot_words(list_object)

def test_integration():
    """Test count_words() and plot_words() workflow."""
    counts = pdgarg1.count_words("tests/einstein.txt")
    fig = plot_words(counts)
    assert isinstance(fig, matplotlib.container.BarContainer), \
           "Wrong plot type"
    assert len(fig.datavalues) == 10, \
           "Incorrect number of bars plotted"
    assert max(fig.datavalues) == 2, "Highest word count should be 2"