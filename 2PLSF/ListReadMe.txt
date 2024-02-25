2PLSF - 无饥饿的两阶段锁
	代码的 stms/ 文件下实现了以下的分布式事务管理算法：
		TinySTM.hpp and tinystm/    Wrapper of TinySTM with the LSA concurrency control
		TL2ORig.hpp and tl2-x86/    Wrapper of the original TL2 concurrency control implementation
		zardoshti/orec_eager_wrap.hpp    Wrapper of the OREC eager STM
		zardoshti/orec_lazy_wrap.hpp    Wrapper of the OREC lazy STM
		zardoshti/tl2_wrap.hpp    Wrapper of the TL2 implementation by Zardoshti et al
		zardoshti/tlrw_eager_wrap.hpp    Wrapper of the TLRW implementation by Zardoshti et al
		OneFileWF.hpp    OneFile Wait-Free STM
		2PLSF.hpp    2PLSF Software Transactional Memory
		2PLUndo.hpp    2PL with Undo and non-scalable reader-writer lock
		2PLUndoDist.hpp    2PL with Undo and scalable reader-writer lock
	代码中的DBx1000 基准测试的源代码取自 https://github.com/yxymit/DBx1000，在此基础上添加了2PLSF 并发控制，除了 DBx1000/ 中添加的文件外，还需要文件 stms/2PLSF.hpp

运行代码
	实验环境搭建
		1.在Ubuntu22.04下安装miniconda后创建虚拟环境conda create -n py27 python=2.7。
		2.先执行sudo apt update以更新软件包列表，执行sudo apt install gcc-10 g++-10以安装GCC 10及其相关的软件包。
		3.若系统上存在其他版本gcc，可执行sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-10 100 --slave /usr/bin/g++ g++ /usr/bin/g++-10来将GCC 10设置为默认版本。
		4.执行gcc –v命令以验证gcc版本。
		5.执行以下命令安装所需工具
			sudo apt-get install gnuplot
			sudo apt-get install texlive-font-utils
		6.执行conda activate py27进入conda虚拟环境，执行以下命令安装包
			pip install wheel
			pip install sqlite
			pip install ncurses
			pip install zlib
	数据结构基准测试部分
		1.将源码压缩包2PLSF.zip上传到Ubuntu服务器合适的目录（如/home下），进入该目录执行unzip 2PLSF.zip将源码解压到当前目录下并进入2PLSF目录。
		2.执行cd stms/tinystm进入文件，执行make对TinySTM进行编译，接着执行cd ../tl2-x86进入后执行make对TL2进行编译，最后cd ../../graphs执行make对数据结构基准进行编译。
		3.在/graphs文件下，运行python2 run-all.py以运行数据结构实验。
	DBx1000基准测试部分
		1.选择不同的并发控制算法，可打开 DBx1000/config.h 并将 CC_ALG 替换为其他名称之一：WAIT_DIE、NO_WAIT、DL_DETECT、SILO、HEKATON、TICTOC、TWO_PL_SF。
		2.在编辑好 config.h 文件后，执行 make -j 命令进行编译。
		3.运行 ./run-dbx1000.py 或 ./rundb 命令进行DBx1000基准测试。
	数据可视化部分
		1.执行完实验后，可对实验结果进行可视化成折线图表示。
		2.首先确保
			sudo apt-get install gnuplot
			sudo apt-get install texlive-font-utils
		以上两条命令以正确执行，以上命运用于安装gnuplot和epstopdf。
		3.进入 graphs/plots 文件夹并运行 ./plot-all.sh 来将文件/graphs/data下数据绘制成如下图的折线图，折线图以pdf的格式存在/plots文件下。

		
