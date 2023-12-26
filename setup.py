from setuptools import setup, find_packages

setup(
    name='LSPLifesaver',  # 包名
    version='0.1',  # 版本号
    author='Christian Lee',  # 作者
    author_email='chrisliyuhan@gmail.com',  # 作者邮箱
    description='A toolset that simplifies the process of solving TSP (Traveling Salesman Problem) problems. ',  # 简短描述
    long_description=open('README.md').read(),  # 长描述，通常是 README 文件的内容
    long_description_content_type='text/markdown',  # 长描述的格式（例如 Markdown）
    url='https://github.com/lxbme/TSPLifesaver',  # 项目主页
    packages=find_packages(),  # 自动发现并包含所有子包
    install_requires=[],
    classifiers=[
        # 分类信息，有助于在 PyPI 等地方正确分类和发现您的包
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Python 版本要求
)

