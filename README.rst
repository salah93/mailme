# Mail Client

## Get Gmail App Password
Setup app password for gmail account [here](https://security.google.com/settings/security/apppasswords)

## Install

```bash
python setup.py install
```


## Usage

```python
from mailme import Mail, PayloadBuilder

results = 'long results...'
payload = (
    PayloadBuilder('salah ahmed')
    .add_subject('Mail from python')
    .add_message(results)
    .add_attachment('results.csv')
    .add_attachment('results.pdf')
    .get_payload()
)

em_address = 's@gmail.com'
password = 'abc123'
to_em_address = 'b@gmail.com'
client = Mail(em_address, password)
client.send([to_em_address], payload)
```
