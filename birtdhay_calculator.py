# Manuel Corral Ledezma
# mcorralledezma@dmacc.edu
# October 16, 2019
import datetime


def half_birtday(birthdate):
    return birthdate + datetime.timedelta(days=182)


if __name__ == '__main__':
    user_date = datetime.datetime(2019, 4, 22)
    print(half_birtday(user_date))
