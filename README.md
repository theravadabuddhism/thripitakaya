# Thipitakaya

> The aim of this project is to preserve the pure `Pali canon` (`Theravada Thripitaka`) in digital format.

## Introduction
Several (partial) text versions of the `Pali canon` already exists. However there are following problems:
- Correctness of the contents is not guaranteed (mainly due to typing mistakes)
- There is no efficient/straight-forward way of correcting any spotted errors
- Different versions are not centrally maintained: fixing an error in one version does not effect the others.

This project mainly aims to address the above issues by providing a central and open repository.

## What does the project contain?
This project contains electronic version the `Pali canon` in raw text format.

## Which edition?
`Sinhala` text will follow the pure `Buddha Jayanthi Tripitaka` edition.

## What is the value of using raw text format?
- Easy to review and edit (compared to most other formats)
- Raw text is the most friendly format for version controlling systems
- Change history is clearly visible to everyone (an essential feature in guaranteeing the authenticity of the content).
- Ability to programmatically parse/convert text files into any other format (`pdf`, `html`, `epub` etc..) with minimum effort.

## Why Github?

Amount of contents of the `Pali canon` is huge. Therefore the contribution of volunteers is heavily needed. 

Contributors can create pull requests with the suggested change and they will be added to the main branch after a proper review.

## How can I contribute?

There are two ways to contribute:
1. By spotting errors
2. By adding missing contents

## How can I submit my contribution?

There are two ways to submit any change/addition:
1. Creating a `github` pull request
2. Reaching via email

The preferred method is creating a `github` pull request with proposed change. However the contributors who are unable to do so can still inform us via email.

![email](https://raw.githubusercontent.com/theravadabuddhism/thripitakaya/develop/readme/resources/email.jpg)


# Technical Details
## Standards
### Directory structure
- Directory hierarchy follows the hierarchy of the Pali canon
- Each directory contains a file named `CONTENTS.json` defining the directory content.
> `CONTENTS.json` is kept to help programmatically parsing the contents

### Text file structure
- First line of file is the title of the Sutta/book (e.g.`බ්‍රහ්මජාල සූත්‍රය`)
- Each section is followed by two blank lines
- If a section has multiple paragraphs, they are separated by single blank line.
- Each section is started with the character `#` followed by the section number (e.g.`#1`)
- Each line of a section/paragraph ends with a new line.

E.g
```
බ්‍රහ්මජාල සූත්‍රය


#1
මා විසින් මෙසේ අසන ලදී: එක් සමයෙක්හි භාග්‍යවතුන් වහන්සේ පන්සියක් පමණ වූ මහත් බික්සඟන සමඟ රජගහනුවරටත් නාලන්දා නුවරටත් අතරෙහි දීර්ඝමාර්ගයට පිළිපන්සේක් වෙති.
සුප්පිය නම් පිරිවැජියාත් බඹදත් නම් තරුණ අතැවැස්සා සමඟ රජගහ නුවරටත් නාලන්දා නුවරටත් අතරැ වූ දික් මඟට පිළිපන්නේ වේ.
...
මෙසේ ඒ ඇදුරු අතැවැසි දෙදෙන එකෙක් අනෙකාට ඉඳුරා ම විරුද්ධවාද ඇත්තෝ භාග්‍යවතුන් වහන්සේත් බික්සඟපිරිසත් අනුව ගියෝ වෙත්.


#2
ඉක්බිති භාග්‍යවතුන් වහන්සේ අම්බලට්ඨිකා උයනෙහි රාජාගාරයෙහි (රජ ගෙහි) බික්සඟන සමඟ එක් රැයක් නවාතැනට එළැඹිසේක.
...
...
#4
එ කල්හි භාග්‍යවතුන් වහන්සේ ඒ භික්ෂූන්ගේ මේ කථාව දැන, නිෂීදනශාලාව කරා එළැඹිසේක.
එළැඹ, පණවන ලද අස්නෙහි හිඳගත් සේක.
හිඳ ගෙන ම, භික්ෂූන් අමතා “මහණෙනි, තෙපි දැන් කවර කථාවෙකින් හුන්නෝ වහු ද? කවර නම් අතුරු කථාවෙක් තොප විසින් අඩාළ කරන ලද දැ?” යි විචාරා වදාළ සේක.

මෙසේ වදාළ කල්හී, ඒ භික්ෂුහු “වහන්ස, මෙහි රෑ අලුයම්හි නැගී සිටි, නිෂීදනශාලායෙහි රැස් ව හුන් අප අතරැ මේ කථාව පහළ විය: ‘ඇවැත්නි, සත්ත්වයන්ගේ ආශයානුශය දන්නා, සියල්ල දක්නා, ඒ භාග්‍යවත් අර්හත් සම්‍යක්සම්බුද්ධයන් වහන්සේ විසින් සත්ත්වයන් එකකු අනෙකකුට වෙනස් අදහස් ඇති නියා කොතරම් මැනවින් දන්නා ලද ද’ යන මෙය ආශ්චර්ය ය, අද්භූත ය.
...
```
