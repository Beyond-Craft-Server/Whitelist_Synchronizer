import time


whitelist_path = ''
command = '!!whitelist sync'


def get_whitelist(server):
    """通过指令获取白名单"""
    server.execute('whitelist list')


def server_output_to_list(info):
    """将服务器返回的白名单转换为列表"""
    full_whitelist = list(info.content.split('[')[1].split(']')[0].split(', '))
    return full_whitelist


def add_new_ID(whitelist):
    """将新ID加入白名单"""
    with open(whitelist_path) as wl:
        whitelist_new = list(wl.read().split('\n'))
        for ID in whitelist:
            if ID not in whitelist_new:
                whitelist_new.append(ID)
            else:
                pass
        return whitelist_new


def write_file(whitelist):
    """写入白名单文件"""
    open(whitelist_path, 'w').close()
    with open(whitelist_path, 'a') as wl:
        for ID in whitelist:
            if ID != '':
                wl.write('{}\n'.format(ID))


State = False
def on_info(server, info):
    global State
    if info.content == command and info.is_player:
        get_whitelist(server)
        State = True
        time.sleep(1)
        State = False
        server.reply(info, '§a白名单同步完成')
    if info.content.startswith('Whitelist: [') and not info.is_player and State:
        write_file(add_new_ID(server_output_to_list(info)))
