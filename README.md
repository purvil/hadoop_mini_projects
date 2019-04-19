# Hadoop Mini projects
* Here, I have implemented Map-Reduce programs in python which is run using Hadoop Streaming. Hadoop streaming is API for Hadoop to run Map-reduce program in any lnaguage as long as it can read standard input and write to standard output.

### Dataset
Data files are located [here](https://github.com/purvil/hadoop_mini_projects/tree/master/data).

### How to run map-reduce program
- Install [cloudera quickstart VM](https://www.cloudera.com/downloads/quickstart_vms/5-13.html), which is pseudo distributed system.
- open terminal
- First of all we have to copy our data to hdfs.
- `hadoop fs -put /path/to/data/file/in/local/file/system path/of/destination/in/hdfs`
- `hadoop jar /usr/hdp/2.3.6.0-3796/hadoop-mapreduce/hadoop-streaming-2.7.1.2.3.6.0-3796.jar -mapper /path/to/mapper/in/local/file/system/mapper.py -reducer /path/to/mapper/in/local/file/system/reducer.py -file /path/to/mapper/in/local/file/system/mapper.py -file /path/to/mapper/in/local/file/system/reducer.py -input path/to/input/file/in/hdfs -output path/to/output/directory/in/hdfs` Version of jar file may change depends on your hadoop version
- Your output will be in `path\to\output\directory\in\hdfs\part-00000` to check it execute `hadoop fs -cat path\to\output\directory\in\hdfs\part-00000`
