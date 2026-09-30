package com.example.a3_1module_3handson2.model

data class SearchResponse(
    val error: Boolean,
    val query: String?,
    val results: List<DocumentResult>?,
    val count: Int?,
    val groq_configured: Boolean?,
    val message: String?
)