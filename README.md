# Courier Delivery Service API

This repository contains the source code for a RESTful API for a courier delivery service. The API enables users to manage and track parcel deliveries, including features such as courier assignment, parcel tracking, and delivery confirmation with image upload.

## Tech Stack

- **Backend Framework:** Django & Django Rest Framework
- **Authentication:** JWT with djangorestframework-simplejwt
- **Documentation:** Swagger with DRF YASG
- **Database:** Postgres (for development purposes)

## Permissions & Roles

- **Customers:** Can create parcels, view their parcel status, and confirm delivery.
- **Couriers:** Assigned parcels, update parcel status, upload delivery proof.
- **Admins:** Full access to all records and user management.

## Features

- **JWT Authentication:** Use SimpleJWT for handling user authentication.
- **Parcel Management:** CRUD operations for parcel handling.
- **Permissions & Roles:** Custom permissions for different user roles.
- **Pagination & Filtration:** Add pagination to parcel lists and allow filtering by status, sender, receiver, and courier.
- **Image Upload for Delivery Proof:** Couriers can upload an image as proof of delivery.
- **Viewsets & Routers:** Use DRF viewsets and routers for efficient URL routing.
- **Swagger Documentation:** Use DRF YASG for auto-generated Swagger API documentation.
