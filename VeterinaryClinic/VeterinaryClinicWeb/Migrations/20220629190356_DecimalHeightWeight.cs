using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace VeterinaryClinicWeb.Migrations
{
    public partial class DecimalHeightWeight : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<decimal>(
                name: "Weight",
                table: "Animal",
                type: "decimal(10,3)",
                nullable: false,
                oldClrType: typeof(float),
                oldType: "float(10)");

            migrationBuilder.AlterColumn<decimal>(
                name: "Height",
                table: "Animal",
                type: "decimal(5,2)",
                nullable: false,
                oldClrType: typeof(float),
                oldType: "float(5)");
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AlterColumn<float>(
                name: "Weight",
                table: "Animal",
                type: "float(10)",
                nullable: false,
                oldClrType: typeof(decimal),
                oldType: "decimal(10,3)");

            migrationBuilder.AlterColumn<float>(
                name: "Height",
                table: "Animal",
                type: "float(5)",
                nullable: false,
                oldClrType: typeof(decimal),
                oldType: "decimal(5,2)");
        }
    }
}
