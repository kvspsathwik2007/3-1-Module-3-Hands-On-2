package com.example.a3_1module_3handson2

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.ProgressBar
import android.widget.TextView
import android.widget.Toast

import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

import com.example.a3_1module_3handson2.model.SearchRequest
import com.example.a3_1module_3handson2.network.RetrofitClient
import com.example.a3_1module_3handson2.ui.SearchAdapter

import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {

    private lateinit var etQuery: EditText
    private lateinit var btnSearch: Button
    private lateinit var btnClear: Button
    private lateinit var progressBar: ProgressBar

    private lateinit var tvQueryLabel: TextView
    private lateinit var tvStatus: TextView

    private lateinit var recyclerView: RecyclerView

    private lateinit var searchAdapter: SearchAdapter

    override fun onCreate(
        savedInstanceState: Bundle?
    ) {

        super.onCreate(savedInstanceState)

        setContentView(
            R.layout.activity_main
        )

        initializeViews()

        setupRecyclerView()

        setupListeners()
    }

    private fun initializeViews() {

        etQuery =
            findViewById(R.id.etQuery)

        btnSearch =
            findViewById(R.id.btnSearch)

        btnClear =
            findViewById(R.id.btnClear)

        progressBar =
            findViewById(R.id.progressBar)

        tvQueryLabel =
            findViewById(R.id.tvQueryLabel)

        tvStatus =
            findViewById(R.id.tvStatus)

        recyclerView =
            findViewById(R.id.recyclerView)
    }

    private fun setupRecyclerView() {

        searchAdapter =
            SearchAdapter()

        recyclerView.layoutManager =
            LinearLayoutManager(this)

        recyclerView.adapter =
            searchAdapter
    }

    private fun setupListeners() {

        btnSearch.setOnClickListener {

            performSearch()
        }

        btnClear.setOnClickListener {

            clearSearch()
        }
    }

    private fun performSearch() {

        val query =
            etQuery.text
                .toString()
                .trim()

        if (query.isEmpty()) {

            etQuery.error =
                "Please enter a query"

            tvStatus.text =
                "Enter a query to search documents."

            return
        }

        searchAdapter.clearDocuments()

        tvQueryLabel.text =
            "Query: $query"

        tvStatus.text =
            "Searching..."

        showLoading(true)

        lifecycleScope.launch {

            try {

                val response =
                    RetrofitClient
                        .apiService
                        .searchDocuments(
                            SearchRequest(query)
                        )

                if (!response.isSuccessful) {

                    showError(
                        "Server error: ${response.code()}"
                    )

                    return@launch
                }

                val searchResponse =
                    response.body()

                if (searchResponse == null) {

                    showError(
                        "Empty response from backend."
                    )

                    return@launch
                }

                if (searchResponse.error) {

                    showError(
                        searchResponse.message
                            ?: "Search failed."
                    )

                    return@launch
                }

                val results =
                    searchResponse.results
                        ?: emptyList()

                if (results.isEmpty()) {

                    tvStatus.text =
                        "No relevant documents found."

                    return@launch
                }

                searchAdapter.updateDocuments(
                    results
                )

                tvStatus.text =
                    "${results.size} relevant documents found."

            } catch (exception: Exception) {

                showError(
                    "Backend unavailable.\n" +
                            "Make sure Flask is running."
                )

            } finally {

                showLoading(false)
            }
        }
    }

    private fun clearSearch() {

        etQuery.text.clear()

        etQuery.error = null

        tvQueryLabel.text =
            "Query:"

        tvStatus.text =
            "Enter a query to search documents."

        searchAdapter.clearDocuments()
    }

    private fun showLoading(
        loading: Boolean
    ) {

        progressBar.visibility =
            if (loading) {
                View.VISIBLE
            } else {
                View.GONE
            }

        btnSearch.isEnabled =
            !loading

        etQuery.isEnabled =
            !loading
    }

    private fun showError(
        message: String
    ) {

        tvStatus.text =
            message

        Toast.makeText(
            this,
            message,
            Toast.LENGTH_LONG
        ).show()
    }
}