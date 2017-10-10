
# pull in TF methods
from __main__ import F, T, L, E

def is_weqt(verb_node):
    '''
    Validate whether a given verb_node (word_node in TF) is a weqetal.
    Only the qatal, or perfect is stored in the ETCBC database.
    Typicaly the weqetal is set apart by being in discourse
        with an attached waw.
        
    Requires following BHSA features to be loaded
        vt lex domain
    '''

    tense = F.vt.v(verb_node)
    clause = L.u(verb_node, otype='clause')[0]

    # check if tense is perfect
    if tense != 'perf':
        return False

    # begin looking for features of weqetal
    # get clause domain
    domain = F.domain.v(clause)
    
    # look for attached waw in preceding word
    lex_before = L.u(verb_node-1, otype='lex')[0] # lex obj of preceding
    attached_waw = True if F.lex.v(lex_before) == 'W' else False
    
    # weqetal if there is a waw anddomain is discursive/quotation
    if attached_waw and domain in {'D', 'Q'}:
        return True
    else:
        return False
