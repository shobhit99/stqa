### Windows :

firefox 64 bit driver : https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win64.zip
firefox 32 bit driver : https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-win32.zip

extract and copy executable in same directory as runtest.py

### Linux

firefox 64 bit : https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
firefox 32 bit : https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux32.tar.gz

export PATH=$PATH:/path/to/executable/dir


### Test Case format
> delimiter is ;
#### register.txt
```
first name;last name;email;mobile no;address without semicolon;password;repeat password;gender;blood group;date of birth
```
>> Example
```
rohit;sharma;rohitsharma@gmail.com;8284848593;Bandra,Mumbai;password1234;password1234;Male;O+;1989/10/12
```

#### view.txt
```
email;password
```

## Usage :
```python
python runtest.py register

python runtest.py view
```
### Output :
```
output_register.txt
output_view.txt
```