using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using VeterinaryClinic.BL;

namespace VeterinaryClinicWeb.Mappings
{
    public class VetMap : IEntityTypeConfiguration<Vet>
    {
        public void Configure(EntityTypeBuilder<Vet> builder)
        {
            builder.ToTable("Vet");

            builder.Property(p => p.CouncilNumber)
                .HasColumnType("int")
                .IsRequired();

            builder.Property(p => p.Gender)
                .HasColumnType("varchar(6)")
                .HasConversion<string>();
        }
    }
}
