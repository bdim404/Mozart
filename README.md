# Music Score Recognition API

基于 FastAPI 的乐谱识别服务，可以将五线谱图片转换为简谱标注。

## 环境要求

- Python 3.7+
- Conda

## 安装步骤

### 1. 创建 Conda 环境

```bash
conda create -n omr_api python=3.8
conda activate omr_api
```

### 2. 安装依赖

```bash
pip install fastapi uvicorn python-multipart pillow opencv-python scikit-image scipy numpy
```

如果项目有 requirements.txt：
```bash
pip install -r requirements.txt
```

## 启动服务

```bash
conda activate omr_api
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

服务启动后访问：
- API 地址: http://localhost:8000
- API 文档: http://localhost:8000/docs

## API 使用

### POST /process

上传乐谱图片，返回标注后的图片。

**请求示例：**

```bash
curl -X POST "http://localhost:8000/process" \
  -F "file=@testcases/01.PNG" \
  --output result.png
```

**Python 示例：**

```python
import requests

with open('testcases/01.PNG', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/process', files=files)

with open('result.png', 'wb') as f:
    f.write(response.content)
```

**响应：**
- Content-Type: image/png
- 返回标注了简谱（1-7）的图片

### GET /

健康检查端点。

```bash
curl http://localhost:8000/
```

**响应：**
```json
{"message": "Music Score Recognition API"}
```

## 项目结构

```
.
├── api.py              # FastAPI 服务主文件
├── src/
│   ├── main.py         # 核心识别逻辑
│   └── ...
└── testcases/          # 测试用例图片
```
