library(ggplot2)

#SRR8427257_1
pd1 <- read.csv('/Users/apple/Desktop/SRR8427257_1_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p1 <- ggplot(data = pd1, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR8427257_1")+
  ylab('log of TPM')+
  xlab('PI')
p1
ggsave(p1, file="SRR8427257_1.eps", device="eps")


#SRR8427258_1
pd2 <- read.csv('/Users/apple/Desktop/SRR8427258_1_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p2 <- ggplot(data = pd2, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR8427258_1")+
  ylab('log of TPM')+
  xlab('PI')
p2
ggsave(p2, file="SRR8427258_1.eps", device="eps")


#SRR9847854_1
pd3 <- read.csv('/Users/apple/Desktop/SRR9847854_1_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p3 <- ggplot(data = pd3, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
  'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR9847854_1")+
  ylab('log of TPM')+
  xlab('PI')
p3
ggsave(p3, file="SRR9847854_1.eps", device="eps")

#SRR9847855_1
pd4 <- read.csv('/Users/apple/Desktop/SRR9847855_1_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p4 <- ggplot(data = pd4, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR9847855_1")+
  ylab('log of TPM')+
  xlab('PI')
p4
ggsave(p4, file="SRR9847855_1.eps", device="eps")

###illumina
##1
#SRR3116182
pd5 <- read.csv('/Users/apple/Desktop/SRR3116182_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p5 <- ggplot(data = pd5, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR3116182")+
  ylab('log of TPM')+
  xlab('PI')
p5
ggsave(p5, file="SRR3116182.eps", device="eps")


#SRR7510550
pd6 <- read.csv('/Users/apple/Desktop/SRR7510550_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p6 <- ggplot(data = pd6, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR7510550")+
  ylab('log of TPM')+
  xlab('PI')
p6
ggsave(p6, file="SRR7510550.eps", device="eps")


#SRR7510557
pd7 <- read.csv('/Users/apple/Desktop/SRR7510557_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p7 <- ggplot(data = pd7, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR7510557")+
  ylab('log of TPM')+
  xlab('PI')
p7
ggsave(p7, file="SRR7510557.eps", device="eps")


#SRR7510578
pd8 <- read.csv('/Users/apple/Desktop/SRR7510578_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p8 <- ggplot(data = pd8, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR7510578")+
  ylab('log of TPM')+
  xlab('PI')
p8
ggsave(p8, file="SRR7510578.eps", device="eps")


##2
#SRR6311991
pd9 <- read.csv('/Users/apple/Desktop/SRR6311991_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p9 <- ggplot(data = pd9, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR6311991")+
  ylab('log of TPM')+
  xlab('PI')
p9
ggsave(p9, file="SRR6311991.eps", device="eps")

#SRR6312008
pd10 <- read.csv('/Users/apple/Desktop/SRR6312008_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p10 <- ggplot(data = pd10, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR6312008")+
  ylab('log of TPM')+
  xlab('PI')
p10
ggsave(p10, file="SRR6312008.eps", device="eps")


##3
#SRR7963131
pd11 <- read.csv('/Users/apple/Desktop/SRR7963131_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p11 <- ggplot(data = pd11, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR7963131")+
  ylab('log of TPM')+
  xlab('PI')
p11
ggsave(p11, file="SRR7963131.eps", device="eps")


##4
#SRR8731662
pd12 <- read.csv('/Users/apple/Desktop/SRR8731662_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p12 <- ggplot(data = pd12, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR8731662")+
  ylab('log of TPM')+
  xlab('PI')
p12
ggsave(p12, file="SRR8731662.eps", device="eps")


#SRR8731670
pd13 <- read.csv('/Users/apple/Desktop/SRR8731670_plot_DF_R_log.tsv', sep='\t', header = FALSE)
p13 <- ggplot(data = pd13, aes(x= V1, y = V2))+geom_boxplot()+
  scale_x_discrete(limits=c('box_0','box_1','box_2','box_3','box_4','box_5','box_6','box_7','box_8',
                            'box_9','box_10','box_11','box_12','box_13','box_14','box_15','box_16','box_17'))+
  theme(axis.text.x = element_text(angle = 45, hjust = 0.5, vjust = 0.5))+
  labs(title = "SRR8731670")+
  ylab('log of TPM')+
  xlab('PI')
p13
ggsave(p13, file="SRR8731670.eps", device="eps")






#concat all plots
library(ggpubr)
ptotal <- ggarrange(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
ptotal
ggsave(ptotal, file="all_plots.eps", device="eps")


