@echo off
echo �������Զ�ֿ̲�
pause
move %~dp0\.git\config %~dp0\
rd /s/q %~dp0\.git

git init
del %~dp0\.git\config
move %~dp0\config %~dp0\.git\
git add .
git commit -m "initiation"
git push -u gitee master
pause