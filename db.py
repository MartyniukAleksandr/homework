from tabulate import tabulate
from random import randint


def FileManager(db_path):
    """
    :param db_path: string
    :return:
    """
    def parse_data(text=''):
        rows = text.split('\n')
        result = []
        for row in rows:
            result.append(row.split(';'))
        return result

    def write(data):
        try:
            with open(db_path,'a') as f:
                f.write(data)
                f.write("\n")
        except FileNotFoundError:
            print(f"File is not found {db_path}")

        return f"Write: {str(data)}"

    def read():
        try:
            file = open(db_path)
            data = file.read()
            file.close()
            return parse_data(data)
        except Exception as e:
            print(e)

    def update(id, data):
        try:
            with open(db_path, 'r') as f: # открываем файл для чтения
               file = f.readlines() # читаем построчно

            for x in range(len(file)): # цикл, который проходит по всем строкам...
                if str(id) in file[x]: # сравниваем наш id с id новой строки....
                    file[x] = data # если он совпадает(есть такое значения в строке) то переопределяем данные...

            with open(db_path, 'w') as line: # и записываем их в файл
                line.write(''.join(file))

        except FileNotFoundError:
            print(f"File is not found {db_path}")

    def delete(data):
        with open(db_path, 'w') as f:
            f.write(data)

    return {
        'write': write,
        'read': read,
        'update': update,
        'delete': delete
    }
# ORM - own system
def UserDB(fm = FileManager("email.csv")):
    """
    :param fm: {
        'write': function,
        'read': function,
        'update': function,
        'delete': function
    }
    :return:
    """
    required_fields = ['login_email', 'first_name', 'last_name']
    def add(*data, **kwargs):

        try:
            # validation step start
            counter = 0
            for x in kwargs:
                if kwargs[x] == "":
                    raise Exception(f"{x} is required! Please enter an value!")
                if x in required_fields:
                    counter += 1
            if counter != 3:
                raise Exception(f"You must include all required fields: {','.join(required_fields)}\n")
            # validation step end
            user_entity = ''
            kwargs['identifier'] = randint(1_000, 1_0000)
            payload = {
                0: kwargs['login_email'],
                1: kwargs['identifier'],
                2: kwargs['first_name'],
                3: kwargs['last_name']
            }
            for field in payload:
                user_entity += str(payload[field]) + ";"
            fm['write'](user_entity)
            return "You successfully added new user to database..."
        except Exception as e:
            print(e)

    def update(id, **kwargs):
        user_id = get_by_id(id) # используем функцию для получени id

        try:
            # validation step start
            counter = 0
            for x in kwargs:
                if kwargs[x] == "":
                    raise Exception(f"{x} is required! Please enter an value!")
                if x in required_fields:
                    counter += 1
            if counter != 3:
                raise Exception(f"You must include all required fields: {','.join(required_fields)}\n")

            # validation step end
            for row in user_id:
                row[0] = kwargs['login_email']
                row[2] = kwargs['first_name']
                row[3] = kwargs['last_name']

            result = ';'.join(row)+'\n'

            fm['update'](id, result)

            return "You successfully update user to database..."
        except Exception as e:
            print(e)

    def get_all(*data, **kwargs):
        return fm['read']()

    def get_by_id(id):
        rows = fm['read']()
        result = []
        for row in rows[1:]:
            if int(row[1]) == int(id):
                result.append(row)
                break
        result.insert(0, rows[0])
        return result

    def remove_by_id(id):
        rows = fm['read']()[1:-1]
        headlines = fm['read']()[0] # вытащим заголовки таблици

        def filter_cb(row):
            return int(row[1]) != int(id)

        updated_list = list(filter(filter_cb, rows))

        result = ';'.join(headlines)+'\n' # записываем заголовки таблици, переобразовав в строку
        for row in updated_list:
            result += ';'.join(row)+'\n' # записываем новый результат без значенния, который был удален, переобразовав в строку

        fm['delete'](result)

    return {
        'add': add,
        'update': update,
        'get_all': get_all,
        'remove_by_id': remove_by_id,
        'get_by_id': get_by_id
    }


def render_table(data):
    print(tabulate(data[1:], headers=data[0]))


db = UserDB()

#Delete user by ID from database
# db['remove_by_id'](2070)

# Add user from database
# db['add'](login_email = "foo@gmail.com", first_name="John", last_name="Bradshaw")

# Update User from database
# db['update'](4081, login_email = "foo@gmail.com", first_name="Alex", last_name="Martyniuk")

# Get user by id or get all users from database
# render_table(db['get_all']())
# render_table(db['get_by_id'](9346))