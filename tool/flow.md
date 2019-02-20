## latex公式
\[
e ^ {i\pi} + 1 = 0
\]


## [Atom-使用Markdown画流程图](https://blog.csdn.net/jiaobuchong/article/details/78484387?fps=1&locationNum=4)
## [flowchart教程](https://mermaidjs.github.io/flowchart.html)
## [mermaid说明](https://mermaidjs.github.io/)
## [html(draw.io)绘制流程图地地址](https://www.draw.io/)
## [思维导图工具xmind]
```mermaid
graph TD
A[image] -->B{image is null?}
B-->|no|B1[detect.net_forward]
B-->|yes|A
B1 --> D[caffewrapper.forward]
D -->B1

B1 -->B2{forward is success?}
B2-->|no|A
B2-->|yes|B3[Result]
B3-->|history_featuremap|B1
