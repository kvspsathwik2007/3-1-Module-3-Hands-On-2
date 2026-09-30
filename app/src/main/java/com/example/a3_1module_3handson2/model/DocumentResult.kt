package com.example.a3_1module_3handson2.model

data class DocumentResult(
    val id: Int,
    val title: String,
    val content: String,
    val similarity: Double
)