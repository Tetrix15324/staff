def Corona_Data():
    data = open('data.txt', 'r+')

    print( '+ {:-<2}{:-^15}{:->20}+'.format('', '', ''))
    print( '|{:^38}|'.format('GETTING DATA....'))
    print( '|{:^35}   |'.format('PLEASE WAIT'))
    print( '+ {:-<2}{:-^15}{:->20}+'.format('', '', ''))

    global world_line, vn_line, time_line, temp
    world_line = data.readline()
    world_line = world_line.replace('\n', '')
    vn_line = data.readline()
    vn_line = vn_line.replace('\n', '')
    time_line = data.readline()
    data.seek(0)
    temp = data.read()
    temp = temp.replace('\n', '')

    url = 'https://news.google.com/covid19/map?hl=vi&gl=VN&ceid=VN%3Avi&mid=%2Fm%2F01crd5'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    world = soup.find('tr', class_ = 'sgXwHf wdLSAe Iryyw').find_all('td')
    viet_nam = soup.find('tr', class_ = 'sgXwHf wdLSAe ROuVee').find_all('td')

    time = datetime.datetime.now()
    time_line = eval(time_line)
    if int(time.strftime('%d')) - int(time_line[0]) == 2:
        data.seek(0)
        data.truncate()
        data.seek(0)

        data.close()
        data = open('data.txt', 'r+')
    else:
        pass

    def compare(a, b):
        temp = []
        for i in range(len(a)):
            if a[i] < b[i]:
                t = 'giảm'
                temp.append((t, (b[i] - a[i])))
            if a[i] > b[i]:
                t = 'tăng'
                temp.append((t, (a[i] - b[i])))
            if a[i] == b[i]:
                t = 'không tăng(giảm)'
                temp.append((t, (a[i] - b[i])))
        return temp


    world_list = []
    for w in world:
        w = str(w)
        w = w.replace(w[0:18], '')
        t = w.find('<')
        w = w[0:t]
        world_list.append(w)

    if str(world_list) != world_line:
        data.write(str(world_list))
    data.write('\n')

    viet_nam_list = []
    for vn in viet_nam:
        vn = str(vn)
        vn = vn.replace(vn[0:18], '')
        t = vn.find('<')
        vn = vn[0:t]
        viet_nam_list.append(vn)

    if str(viet_nam_list) != vn_line:
        data.write(str(viet_nam_list))

    data.write('\n')
    time = [time.strftime('%d'), time.strftime('%m'), time.strftime('%y')]
    time = str(time)
    if time not in temp:
        data.write(time)

    if str(world_list) != world_line or str(world_list) == world_line:
        world_line = eval(world_line)
        world_list_another = world_list.copy()
        for i in range(len(world_line)):
            world_line[i] = int(world_line[i].replace('.', ''))
            world_list_another[i] = int(world_list_another[i].replace('.', ''))

        temp = compare(world_list_another, world_line)

        print( '+{:-^43}+'.format('WORLD'))
        print( '| {:<30} | {:^1}|'.format('Số ca nhiễm', world_list[0]))
        print( '| {:<30} | {:>9}|'.format(temp[0][0], temp[0][1]))
        print( '| {:<1} | {:>9}|'.format('Số ca nhiễm trên 1 triệu người', world_list[1]))
        print( '| {:<30} | {:>9}|'.format(temp[1][0], temp[1][1]))
        print( '| {:<30} | {:>8}|'.format('Số người đã bình phục', world_list[2]))
        print( '| {:<30} | {:>9}|'.format(temp[2][0], temp[2][1]))
        print( '| {:<30} | {:>9}|'.format('Số người tử vong', world_list[3]))
        print( '| {:<30} | {:>9}|'.format(temp[3][0], temp[3][1]))


    if str(viet_nam_list) != vn_line or str(viet_nam_list) == vn_line:
        vn_line = eval(vn_line)
        viet_nam_list_another = viet_nam_list.copy()
        for i in range(len(vn_line)):
            vn_line[i] = int(vn_line[i].replace('.', ''))
            viet_nam_list_another[i] = int(viet_nam_list_another[i].replace('.', ''))

        temp = compare(viet_nam_list_another, vn_line)

        print( '|{:-^43}|'.format('VIỆT NAM'))
        print( '| {:<30} | {:>9}|'.format('Số ca nhiễm', viet_nam_list[0]))
        print( '| {:<30} | {:>9}|'.format(temp[0][0], temp[0][1]))
        print( '| {:<1} | {:>9}|'.format('Số ca nhiễm trên 1 triệu người', viet_nam_list[1]))
        print( '| {:<30} | {:>9}|'.format(temp[1][0], temp[1][1]))
        print( '| {:<30} | {:>9}|'.format('Số người đã bình phục', viet_nam_list[2]))
        print( '| {:<30} | {:>9}|'.format(temp[2][0], temp[2][1]))
        print( '| {:<30} | {:>9}|'.format('Số người tử vong', viet_nam_list[3]))
        print( '| {:<30} | {:>9}|'.format(temp[3][0], temp[3][1]))
        print( '+ {:-<2}---{:-^15}{:->22}+'.format('', '', ''))

    print( '| {:<1}      | {:>2}/{}/{:>1} |'.format('Số liệu được lấy vào ngày', time_line[0],time_line[1], time_line[2]))
    print( '+ {:-<2}---{:-^15}{:->22}+'.format('', '', ''))

    data.close()

print(Corona_Data())