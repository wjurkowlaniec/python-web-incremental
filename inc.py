


data = {
    'money':{
        'amount': 0,
        'rate': 1
    },
    'karma':{
        'amount': 0,
        'rate': 1
    },
    'health':{
        'amount': 0,
        'rate': 2
    },
    'happiness':{
        'amount': 0,
        'rate': 3
    }
}

def ticker():
    for item in data.keys():
        data[item]['amount']+=data[item]['rate']


def update_values():
    for item in data.keys():
        to="{}__value".format(item)
        console.log(to);
        document.getElementById(to).innerHTML = data[item]['amount']

console.log(data);
