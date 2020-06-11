[![Github top language](https://img.shields.io/github/languages/top/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](../../)
[![Codacy grade](https://img.shields.io/codacy/grade/[codacy-proj-id].svg?style=for-the-badge)](https://www.codacy.com/manual/FredHappyface/OcticonsV2Font)
[![Repository size](https://img.shields.io/github/repo-size/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FredHappyface/OcticonsV2Font.svg?style=for-the-badge)](../../commits/master)

# OcticonsV2Font


GitHub Octicons V2

See [fontinfo](fontinfo.md) for more information on the font table


Fonts are under [sfd](sfd/), [ttf](ttf/) and [woff2](woff2/)


## Font generation
I will probably use some scripts for this next time but exporting 6 fonts twice
didn't take too long to do manually


## SFD, TTF and WOFF2

.sfd is the format used by fontforge

.ttf is widely supported as has recently been argued to be superior to cff otf
(still uses open type)

.woff2 to provide web support. Most browsers support this format


## FontForge Challenges and workarounds

FontForge has had some significant challenges importing svgs. The workaround is
as follows:

1. Open the svg in Inkscape
2. Copy the svg to FontForge
3. For 16x16 svgs, scale uniformly by 6250% and move by x=492, y=-492

^ The above seems to fail for batch processing...

See the fonts as above for the previous version. Please note that the font info
will not match up. This is going to go on a backseat until I find a more workable
solution

## Download
### Clone
#### Using The Command Line
1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
```bash
$ git clone https://github.com/FredHappyface/OcticonsV2Font
```

More information can be found at
<https://help.github.com/en/articles/cloning-a-repository>

#### Using GitHub Desktop
1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
<https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop>

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location


## Community Files
### Licence
MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog
See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct
In the interest of fostering an open and welcoming environment, we
as contributors and maintainers pledge to make participation in our
project and our community a harassment-free experience for everyone.
Please see the
[Code of Conduct](https://github.com/FredHappyface/.github/blob/master/CODE_OF_CONDUCT.md) for more information.

### Contributing
Contributions are welcome, please see the [Contributing Guidelines](https://github.com/FredHappyface/.github/blob/master/CONTRIBUTING.md) for more information.

### Security
Thank you for improving the security of the project, please see the [Security Policy](https://github.com/FredHappyface/.github/blob/master/SECURITY.md) for more information.
