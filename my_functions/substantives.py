# pull in TF methods
from __main__ import F, T, L, E

def is_subs(word):
    '''
    Return boolean on whether a word is a substantive at the head of the phrase.
        i.e. a noun without any modifiers.
        Excludes: demonstratives, proper names
        Require word node.
    
    Based on a supplied wordnode get phrase, phrase atom, and subphrase
        features and compare them against a group of sets.
        Define those sets first. Then make the comparison.
    
    Following BHSA features MUST be loaded:
        pdp typ rela function
    
    *Caution* 
    This function works reasonably well,
        but there are a number of edge cases that it does not catch.
        Fine-tuning this function would make a nice notebook in itself.
        See Gen 20:5 for a good edge case example, in which both היא pronouns
        are registered as subjects, but only one should be.
    '''
    
    # keep words with these part of speech tags
    keep_pdp = {'subs'} # substantive

    # exclude words in phrase_atoms with these relation features
    omit_pa_rela = {'Appo', # apposition
                    'Spec'} # specification
    
    # exclude words in subphrases with these relation features
    omit_sp_rela = {'rec', # nomens rectum
                    'adj', # adjectival 
                    'atr', # attributive
                    'mod', # modifier
                    'dem'} # demontrative
                        
    # get word's phrase, phrase atom, and subphrase, and subphrase relations
    w_phrase = L.u(word, otype='phrase')[0] # word's phrase node
    w_phrase_atom = L.u(word, otype='phrase_atom')[0] # word's phrase atom
    w_subphrases = L.u(word, otype='subphrase') # word's subphrase
    w_subphrs_relas = set(F.rela.v(sp) for sp in w_subphrases) # subphrs rela
    
    # compare word/phrase features against the sets
    if all([
            
            # phrase dependent part of speech is valid
            F.pdp.v(word) in keep_pdp,
            
            # phrase_atom relation is valid
            F.rela.v(w_phrase_atom) not in omit_pa_rela,
            
            # subphrase relation is valid
            not w_subphrs_relas & omit_sp_rela,
           ]):
        
        # word is a subject
        return True
    
    else:
        # word is not subject
        return False