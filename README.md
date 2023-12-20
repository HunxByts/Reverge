## Reverge
Tool untuk meng extract dan convert hex pada suatu file, teknik ini biasanya di gunakan pada kompetisi CTF kategory forensik. Tool ini di buat menggunakan Python ``V3++``

<img src="https://github.com/HunxByts/Reverge/blob/main/asset/Screenshot%20from%202023-12-20%2015-39-00.png"/>

### Instalation on Linux (deb)
```
sudo apt-get install git
sudo apt-get install python3
```

### Instalation on Termux
```
pkg install git
pkg install python3
```

### Usage Tool
```
git clone https://github.com/HunxByts/Reverge.git
cd Reverge
pip3 install hexdump
python3 reverge.py -h
```

### Usage options
```
Untuk Extract hexadesimal file : python3 reverge.py -i YOUR_FILE -r -o YOUR_OUTPUT
Untuk Convert hexadesimal ke binary file : python3 reverge.py -i OUTPUT_FILE_HEX -f YOUR_OUTPUT
```
<details>
<summary>:zap: Author :</summary>
- <strong><a href="https://github.com/HunxByts">HunxByts</a></strong>
</details>
