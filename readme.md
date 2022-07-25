# PPGEN
Generates a profile image for a given name.

> Version 0.1.0

## Path Table

| Method | Path | Description |
| --- | --- | --- |
| GET | [/image/{text}](#getimagetext) | Create Image |
| GET | [/counter](#getcounter) | Get Counter |

## Reference Table

| Name | Path | Description |
| --- | --- | --- |
| HTTPValidationError | [#/components/schemas/HTTPValidationError](#componentsschemashttpvalidationerror) |  |
| ValidationError | [#/components/schemas/ValidationError](#componentsschemasvalidationerror) |  |

## Path Details

***


### [GET]/image/{text}

- Summary  
Create Image

#### Parameters(Query)

```ts
width?: integer
```

```ts
height?: integer
```

```ts
color?: string
```

```ts
text_color?: string
```

#### Responses

- 200 Successful Response

`application/json`

```ts
imageurl: string
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [GET]/counter

- Summary  
Get Counter

#### Responses

- 200 Successful Response

`application/json`

```ts
{}
```

## References

### #/components/schemas/HTTPValidationError

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

### #/components/schemas/ValidationError

```ts
{
  loc?: Partial(string) & Partial(integer)[]
  msg: string
  type: string
}
```