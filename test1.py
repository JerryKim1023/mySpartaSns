



# 각 유저는 한명의 유저를 신고, 여러명의 유저 신고가능

# k번 이상 신고된 유저는 이용정지 , 신고한 유저에게 메일전송

# 정지된 유저에게도 정지되면 정지메일 발송


# 유저목록, 유저가 신고하는 id , 유저 신고 카운트 , 신고 당한 카운트 , 정지당한 user 리스트

# id_list =  ["muzi", "frodo", "apeach", "neo"]
# k는 신고당한 카운트 제한횟수

# 신고당한 횟수    /      정지 여부

# doc['key'] = 'value'  딕셔너리 추가 문법
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

def solution(id_list, report, k):
    answer = []
    report_list = []
    reported_list = []
    mail_person = []
    # first_answer = [0 for _ in range(len(id_list))]
    doc = {}
    for i in report:
        reports = i.split()
        doc[reports[0]] = reports[1]
        print(doc)


    # for rep in report:
    #     if rep.split(' ')[1] == 'muzi':
    #         answer[0] = first_answer[0] + 1
    #     elif rep.split(' ')[1] == 'frodo':
    #         answer[1] = first_answer[1] + 1
    #     elif rep.split(' ')[2] == 'apeach':
    #         answer[2] = first_answer[2] + 1
    #     else:
    #         answer[3] = first_answer[3] + 1
    #
    #     return answer


# def solution(id_list, report, k):
#     answer = []
#     return answer

#
# 아이디 리스트가 2개인 것도 고려
# 문제 접근 방식이 틀림




    # for id in id_list:
    #     answer.append(len(id_list))
    # for report in id_list:
    #     if id == id:
    #         pass
    #     elif

    return answer



users =  ["muzi", "frodo", "apeach", "neo"]
reported = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
accused = 2

print(solution(users,reported, accused))

