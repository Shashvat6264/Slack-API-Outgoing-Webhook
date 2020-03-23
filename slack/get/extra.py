def extract_link(text):
    s_ind = text.find('http')
    if s_ind != -1:
        e_ind = text.find('|')
        link =''
        for i in range(s_ind, e_ind):
            link += text[i]
        return link
    else: 
        return '0'
