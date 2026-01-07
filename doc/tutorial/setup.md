conda info --envs

<!-- 创建环境 -->
conda create -n SimpleTF220 python==3.12 tensorflow==2.20

<!-- 下载pip依赖工具 -->
mamba install pipreqs

<!-- 强制导出依赖 -->
pipreqs ./ --force