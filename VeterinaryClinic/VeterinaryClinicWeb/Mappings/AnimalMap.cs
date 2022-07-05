using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class AnimalMap : IEntityTypeConfiguration<Animal>
    {
        public void Configure(EntityTypeBuilder<Animal> builder)
        {
            builder.ToTable("Animal");

            builder.Property(p => p.Name)
                .HasColumnType("varchar(100)")
                .IsRequired();

            builder.Property(p => p.Color)
                .HasColumnType("varchar(20)")
                .IsRequired();

            builder.Property(p => p.Gender)
                .HasColumnType("varchar(6)")
                .HasConversion<string>();

            builder.Property(p => p.Height)
                .HasColumnType("decimal(5,2)");

            builder.Property(p => p.Weight)
                .HasColumnType("decimal(10,3)");

            builder.HasOne(p => p.Race)
                .WithMany()
                .OnDelete(DeleteBehavior.NoAction);

            builder.HasOne(p => p.Responsible)
                .WithMany()
                .OnDelete(DeleteBehavior.NoAction);
        }
    }
}
