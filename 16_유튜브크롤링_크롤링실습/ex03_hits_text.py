hits_text = "심장혈관 막는 '제로'?…기자가 직접 파헤쳐 봤더니 (자막뉴스) / SBS 게시자: SBS 뉴스 6일 전 2분 15초 조회수 970,746회"

print(hits_text.rfind("조회수"))
print(hits_text.rfind("조회수")+4)
start_index = hits_text.rfind("조회수")+4
end_index = hits_text.rfind("회")
print(hits_text[start_index:end_index]) # 939,511
hits = hits_text[start_index:end_index]
hits = int(hits.replace(",", "")) 
print(hits) # 939511