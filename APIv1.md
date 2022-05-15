# API
[toc]
## 1	环境变量

### 默认环境1
| 参数名 | 字段值 |
| ------ | ------ |
|baseUrl|http://127.0.0.1:8000/api|


## 2	API

##### 说明
> 公告部分接口文档



##### 文档版本
```
v1
```


## 3	announcements_list

> GET  /announcements/
### 接口说明
> 公告列表，可以根据作者名、类型过滤，根据标题、正文搜索，根据创建时间、更新时间排序，可分页显示
### 请求参数(Query Param)
| 参数名称 | 描述 |
| ------ | ------ |
|author|作者|
|category|分类|
|search|标题/正文的搜索关键词|
|ordering|按创建时间/修改时间排序|
|page|分页页码|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 描述 |
| ------ | ------ | ------ |
| count|int32|公告总数|
| next|string|下一页地址|
| previous|string|前一页地址|
| results|array[object]|返回结果|
|⇥ id|int32|公告id|
|⇥ created_time|string|公告创建时间|
|⇥ modified_time|string|公告最近修改时间|
|⇥ title|string|公告标题|
|⇥ author|string|公告作者|
|⇥ category|string|公告类型|
|⇥ body|string|公告正文|


## 4	announcements_create

> POST  /announcements/
### 接口说明
> 创建新公告
### 请求体(Request Body)
| 参数名称 | 数据类型 | 不为空 | 描述 |
| ------ | ------ | :----- | ------ |
| id|int32|false|公告id|
| created_time|string|false|公告创建时间|
| modified_time|string|false|公告最近修改时间|
| title|string|true|公告标题|
| author|string|true|公告作者|
| category|string|true|公告类型|
| body|string|true|公告正文|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 描述 |
| ------ | ------ | ------ |
| id|int32|公告id|
| created_time|string|公告创建时间|
| modified_time|string|公告最近修改时间|
| title|string|公告标题|
| author|string|公告作者|
| category|string|公告类型|
| body|string|公告正文|


## 5	announcements_read

> GET  /announcements/{id}/
### 接口说明
> 单篇公告详情
### 地址参数（Path Variable）
| 参数名称 | 描述 |
| ------ | ------ |
|id|公告id|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 描述 |
| ------ | ------ | ------ |
| id|int32|公告id|
| created_time|string|公告创建时间|
| modified_time|string|公告最近修改时间|
| title|string|公告标题|
| author|string|公告作者|
| category|string|公告类型|
| body|string|公告正文|


## 6	announcements_delete

> DELETE  /announcements/{id}/
### 接口说明
> 删除公告
### 地址参数（Path Variable）
| 参数名称 | 描述 |
| ------ | ------ |
|id|公告id|
### 响应体
● 200 响应数据格式：JSON


## 7	announcements_update

> PUT  /announcements/{id}/
### 接口说明
> 更新公告
### 地址参数（Path Variable）
| 参数名称 | 描述 |
| ------ | ------ |
|id| 公告id|
### 请求体(Request Body)
| 参数名称 | 数据类型 | 不为空 | 描述 |
| ------ | ------ | ------ | ------ |
| id|int32|true|公告id|
| created_time|string|false|公告创建时间|
| modified_time|string|false|公告最近修改时间|
| title|string|true|公告标题|
| author|string|true|公告作者|
| category|string|true|公告类型|
| body|string|true|公告正文|
### 响应体
● 200 响应数据格式：JSON
| 参数名称 | 类型 | 描述 |
| ------ | ------ | ------ |
| id|int32|公告id|
| created_time|string|公告创建时间|
| modified_time|string|公告最近修改时间|
| title|string|公告标题|
| author|string|公告作者|
| category|string|公告类型|
| body|string|公告正文|

