---
layout: default
title: Organization Structure | AIIBSCSTEWC – Indian Bank SC/ST Employees Welfare Council
description: Explore the organizational structure of AIIBSCSTEWC, including leadership, committees, and representatives working for the welfare of Indian Bank SC/ST employees across India.
permalink: /organizations
---


<!-- Page Header Start -->
<div class="container-fluid bg-light py-4 mb-4">
  <div class="container text-center"> 
    <h1 class="display-4 mb-3">Organization</h1>
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb justify-content-center mb-0">
        <li class="breadcrumb-item">
          <a href="/" class=" text-decoration-none">Home</a>
        </li>
        <li class="breadcrumb-item active" aria-current="page">
          Organization
        </li>
      </ol>
    </nav>
  </div>
</div>
<!-- Page Header End -->

<div class="container my-5">
  <div class="table-responsive">
    <table class="table table-bordered table-striped align-middle">
      <thead class="table-primary">
        <tr>
          <th>#</th>
          <th>Name</th>
          <th>Designation</th>
          <th>Address</th>
          <th>PF&nbsp;No.</th>
          <th>Mobile&nbsp;No.</th>
          <th>E-mail</th>
          <th>Image</th>
        </tr>
      </thead>
      <tbody>
        {% for member in site.data.team %}
        <tr>
          <td>{{ forloop.index }}</td>
          <td>{{ member.name }}</td>
          <td>{{ member.position }}</td>
          <td>
            {% if member.address %}
              {{ member.address }}
            {% else %}
              —
            {% endif %}
          </td>
          <td>
            {% if member.pf-number %}
              {{ member.pf-number }}
            {% else %}
              —
            {% endif %}
          </td>
          <td>
            {% if member.mobile %}
              <a href="tel:{{ member.mobile }}">{{ member.mobile }}</a>
            {% else %}
              —
            {% endif %}
          </td>
          <td>
            {% if member.email %}
              <a href="mailto:{{ member.email }}">{{ member.email }}</a>
            {% else %}
              —
            {% endif %}
          </td>
          <td width="100">
            {% if member.image %}
              <img src="{{ member.image }}"
                   alt="{{ member.name }}"
                   width="100"
                   height="100"
                   class="img-thumbnail">
            {% else %}
              <span class="text-muted small">No Image</span>
            {% endif %}
          </td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

                     
                  
