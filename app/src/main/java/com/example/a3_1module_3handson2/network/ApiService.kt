package com.example.a3_1module_3handson2.network

import com.example.a3_1module_3handson2.model.SearchRequest
import com.example.a3_1module_3handson2.model.SearchResponse

import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {

    @POST("search")
    suspend fun searchDocuments(
        @Body request: SearchRequest
    ): Response<SearchResponse>
}