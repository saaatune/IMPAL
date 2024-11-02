/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.kitchensync;

/**
 *
 * @author ASUS
 */
public class Recipe {
    final int recipeID;
    private String recipe;
    private String cuisine;
    final String ingridients;
    private int prepTime;
    private int cookingTime;
    
    public Recipe(int recipeID, String recipe, String cuisine, String ingridients, int prepTime, int cookingTime){
        this.recipeID = recipeID;
        this.recipe = recipe;
        this.cuisine = cuisine;
        this.ingridients = ingridients;
        this.prepTime = prepTime;
        this.cookingTime = cookingTime;
    }

    public int getRecipeID() {
        return recipeID;
    }

    public String getRecipe() {
        return recipe;
    }

    public void setRecipe(String recipe) {
        this.recipe = recipe;
    }

    public String getCuisine() {
        return cuisine;
    }

    public void setCuisine(String cuisine) {
        this.cuisine = cuisine;
    }

    public String getIngridients() {
        return ingridients;
    }

    public int getPrepTime() {
        return prepTime;
    }

    public void setPrepTime(int prepTime) {
        this.prepTime = prepTime;
    }

    public int getCookingTime() {
        return cookingTime;
    }

    public void setCookingTime(int cookingTime) {
        this.cookingTime = cookingTime;
    }
    
    public int getTotal(){
        int totalWaktu = getPrepTime() + getCookingTime();
        return totalWaktu;
    }
}
