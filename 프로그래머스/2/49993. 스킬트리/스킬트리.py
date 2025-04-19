def isGoodSkillTree(st, skill):
    idx = 0
    for i in st:
        if idx >= len(skill):
            break
        cur = skill[idx]
        if i in skillSet:
            if i != cur:
                return False
            else:
                idx += 1
    return True

def solution(skill, skill_trees):
    global skillSet
    skillSet = set(skill)
    answer = 0
    
    for st in skill_trees:
        if isGoodSkillTree(st, skill):
            answer += 1
    
    return answer