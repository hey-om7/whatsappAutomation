
# Whatsapp Automation


## API Reference

### ***App.py***
**UseCase:** To run the automator.
#### the Function **initAuto()** has following Parameters

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `theNumberIncorrect` | `string` | **Required**. The copied outer html of numbers |
| `sendMsgList` | `string` | **Required**. The message to be sent! |

```http
  sendMsgList: use ":{}" to imprint emojis
```
### Use this website to get the emoji names in letters
```
https://emojipedia.org/
```

### ***extractNumbers.py***

**UseCase:** To extract the numbers and save to a new text file.

```http
  _saveNumbers()
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `str1`      | `string` | **Required**. The copied outer html of numbers |




## Authors

- [@heyom](https://github.com/hey-om7/)

# -- End --